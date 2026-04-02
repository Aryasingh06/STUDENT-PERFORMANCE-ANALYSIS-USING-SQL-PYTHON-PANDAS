import pyodbc
#import pandas as pd


# Connect to SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=ARYA-SINGH\\SQLEXPRESS;'
    'DATABASE=StudentDB;'
    'Trusted_Connection=yes;'
)

print("connected successfully")

#ANALYSIS
import pandas as pd 
import matplotlib.pyplot as plt
#query = "SELECT * FROM Students"
#df = pd.read_sql(query, conn)# fetch data
#print(df)

#join query
query = """
SELECT s.name, m.subject, m.marks
FROM Students s
JOIN Marks m ON s.student_id = m.student_id
"""

df = pd.read_sql(query, conn)
print(df)

print(df.columns)
#AVERAGE MARKS
avg = df.groupby('name')['marks'].mean()
print("AVERAGE MARKS\n",avg)

#TOPPER
print("\nTopper ",avg.idxmax())

#subject average
sub_avg = df.groupby('subject')['marks'].mean()
print("Subject average\n",sub_avg)

#  low marks
LOW = df[df['marks']<60]
print("LOW MARKS",LOW)

#save as csv 
df.to_csv("librarystudent_data.csv",index=False)

# Graph
#graph1
avg.plot(kind='bar')
plt.title("Average Marks per Student")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()

#graph2 
sub_avg.plot(kind='bar')
plt.title("Subject-wise Average")
plt.xlabel("Subject")
plt.ylabel("Marks")
plt.show()#display the graph on screen.

#conn.close()









