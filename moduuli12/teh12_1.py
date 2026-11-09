import requests
def chuck_norris():
    url = " https://api.chucknorris.io/jokes/random"
    response = requests.get(url, timeout=100 )
    response.raise_for_status()
    data = response.json()
    return data["value"]


print(chuck_norris())
