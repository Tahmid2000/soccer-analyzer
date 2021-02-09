import requests

url = "https://api-football-v1.p.rapidapi.com/v2/players/player/154"

headers = {
    'x-rapidapi-key': "d23bab6737mshb845a2338eedcb2p137711jsnf78fa2d0de2f",
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)