import sqlite3

#connect to the database
conn = sqlite3.connect('student.db')


#create a cursor object to insert data, create table and fetch data from the database
cursor = conn.cursor()


#Create Table
table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES('John', '10th', 'A', 85)")
cursor.execute("INSERT INTO STUDENT VALUES('Alice', '10th', 'B', 90)") 
cursor.execute("INSERT INTO STUDENT VALUES('Bob', '10th', 'A', 78)")
cursor.execute("INSERT INTO STUDENT VALUES('Eve', '10th', 'B', 32)")
cursor.execute("INSERT INTO STUDENT VALUES('Charlie', '10th', 'A', 55)")


print("The inserted data are:")

data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)


#close the connection
conn.commit()
conn.close()