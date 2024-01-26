import mysql.connector

meudb = mysql.connector.connect(host="localhost",user="brendo",
    password="bre123",database="bdjogos")

meucursor = meudb.cursor()
sql = "INSERT INTO tbl_bdjogos(genero,criadores)VALUES(%s,%s)"
valor = ("god of war","STEAM")

valores = ("menicraft","Microsoft store"),("dbz xenoverse","steam"),("darksouls","steam")
meucursor.execute(sql,valor)
meucursor.executemany(sql,valores)
meudb.commit()
print(meucursor.rowcount,"informação inserida.")
