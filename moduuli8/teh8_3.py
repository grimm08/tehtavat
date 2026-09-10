import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ak08mh77',
         autocommit=True
         )

icao1 = input("Anna ensimäinen ICAO-koodi: ")
icao2 = input("Anna toinen ICAO-koodi: ")

sql1 = f"select latitude_deg, longitude_deg from airport where ident ='{icao1}'"
sql2 = f"select latitude_deg, longitude_deg from airport where ident ='{icao2}'"
korsor = yhteys.cursor()

korsor.execute(sql1)
geo1 = korsor.fetchone()

korsor.execute(sql2)
geo2 = korsor.fetchone()

loca = (geo1[0], geo1[1])
locb = (geo2[0], geo2[1])

dist = geodesic(loca, locb).km

print(f"lentokenttein välinen on {dist:.2f} km")