import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ak08mh77',
         autocommit=True
         )

koodi = input("Anna ICAO-koodi: ").upper()
sql = f"select name, iso_region from airport where ident = '{koodi}'"

kursori = yhteys.cursor()
kursori.execute(sql)
outcome = kursori.fetchall()
for line in outcome:
    print(line)