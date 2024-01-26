import mysql.connector
mydb=mysql.connector.connect(host='localhost',
                             user='brendo',
                             password='bre123')
mycursor=mydb.cursor()
mycursor.execute('create database bdjogos')
