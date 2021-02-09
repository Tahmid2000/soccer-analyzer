import requests

url = "https://football-pro.p.rapidapi.com/api/v2.0/players/search/Lionel%20Messi"

querystring = {"tz":"Europe/Amsterdam"}

headers = {
    'x-rapidapi-key': "d23bab6737mshb845a2338eedcb2p137711jsnf78fa2d0de2f",
    'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)