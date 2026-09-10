import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ak08mh77',
         autocommit=True
         )

koodi = input("Anna maakoodi: ").upper()
sql = f"select type, count(*) from airport where iso_country = '{koodi}' group by type"

kursori = yhteys.cursor()
kursori.execute(sql)
outcome = kursori.fetchall()
for line in outcome:
    print(line)
