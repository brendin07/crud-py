import mysql.connector

meudb = mysql.connector.connect(
    host="localhost",
    user="brendo",
    password="bre123",
    database="bdjogos" )

meucursor= meudb.cursor()
meucursor.execute("CREATE TABLE tbl_bdjogos(id INT NOT NULL AUTO_INCREMENT,genero VARCHAR(225), criadores VARCHAR(223),PRIMARY KEY(id))")
