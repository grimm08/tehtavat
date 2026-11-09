import requests

API_KEY = ("d441219f4cbe352c07d14be2467634a6")
url = "https://api.openweathermap.org/data/2.5/weather"

def k_to_c(kelvin):
    celsius = kelvin - 273.15
    return celsius

place = input("Anna paikan nimi: ").strip()

parameters = {"q": place, "appid": API_KEY, "lang":"fi"}

try:
    response = requests.get(url, params= parameters, timeout=30)

    if response.status_code == 404:
        print("paikkakuntaa ei löytynyt.")
    elif response.status_code == 401:
        print("API-avain on virheellinen tai ei ole vielä aktivoittunut.")
    else:
        response.raise_for_status()
        data = response.json()
        saatila = data["weather"][0]["description"]
        lampotila = k_to_c(data["main"]["temp"])
        print(f"Säätila: {saatila}")
        print(f"Lämpötila: {lampotila:.1f} C")
except requests.exceptions.RequestException as virhe:
    print(f"Error: {virhe}")