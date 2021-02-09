import requests
import pandas as pd

url = "https://football-pro.p.rapidapi.com/api/v2.0/players/184798"

querystring = {"include":"stats","tz":"Europe/Amsterdam"}

headers = {
    'x-rapidapi-key': "d23bab6737mshb845a2338eedcb2p137711jsnf78fa2d0de2f",
    'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

df = pd.read_json(response.text)
print(df)