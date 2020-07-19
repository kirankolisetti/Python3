import requests
import pandas as pd

url = requests.get('https://api.exchangerate-api.com/v4/latest/USD').text
df = pd.read_json(url)
print(df)