import mysql.connector

# mydb = connector.connect(host="localhost", user="liopun", passwd="zxc123")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="zxc123",
  database="liopun"
)

mycursor = mydb.cursor()

mycursor.execute("select * from student")

for x in mycursor:
  print(x)