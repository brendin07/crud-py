import mysql.connector

meudb = mysql.connector.connect(
    host="localhost",
    user="brendo",
    password="bre123",
    database="bdjogos")

meucursor = meudb.cursor()
meucursor.execute("SELECT * FROM tbl_bdjogos")
meuresultado = meucursor.fetchall()
for x in meuresultado:
    print(x)
