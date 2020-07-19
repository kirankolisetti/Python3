import requests

x = requests.get('https://datausa.io/api/data?drilldowns=india&measures=Population&year=latest')
print(x.status_code)

print(x.json())
