import requests

responce =requests.get("https://v6.exchangerate-api.com/v6/d10796c7f1f95850ce335142/latest/USD")
print(responce.json()['conversion_rates'])