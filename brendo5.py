import mysql.connector

meudb = mysql.connector.connect(
    host="localhost",
    user="brendo",
    password="bre123",
    database="bdjogos")
meucursor = meudb.cursor()
sql = "UPDATE tbl_bdjogos SET criadores = 'STEAM' WHERE criadores ='Microsoft store'"
meucursor.execute(sql)
meudb.commit()
print(meucursor.rowcount,"informaçao modificada")
