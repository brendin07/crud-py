import mysql.connector

meudb = mysql.connector.connect(
    host="localhost",
    user="brendo",
    password="bre123",
    database="bdjogos")

meucursor = meudb.cursor()
sql = "DELETE FROM tbl_bdjogos WHERE id = '1'"
meucursor.execute(sql)
meudb.commit()
print(meucursor.rowcount, "informação deletada")
