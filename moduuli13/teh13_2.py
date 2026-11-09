from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False

def hae_kentta(icao):
    yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='ak08mh77',
        autocommit=True
    )
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute("select ident, name, municipality from airport where ident = %s", (icao,))
    tulos = cursor.fetchall()
    cursor.close()
    yhteys.close()
    return tulos

@app.route('/kentta/<icao>')
def kentta(icao):
    rivi = hae_kentta(icao.upper())
    if rivi is None:
        return jsonify({"error": "Airport not found", "ICAO": icao.upper()}), 404
    vastaus = {
        "ICAO": rivi["ident"],
        "Name": rivi["name"],
        "Municipality": rivi["municipality"]
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(use_reloader= True, host='127.0.0.1', port=3000)