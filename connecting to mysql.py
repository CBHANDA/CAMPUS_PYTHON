import mysql.connector
cn=mysql.connector.connect(database="ehma",user="root",password="admin@123")
print("connection established")
cn.close()
print("connection closed")