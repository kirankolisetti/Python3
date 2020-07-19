import requests
import pandas as pd
import json



x = requests.get('https://data.nasa.gov/resource/fvg2-eqzv.json').text
#print(x)

df = pd.read_json(x)
print(df)


