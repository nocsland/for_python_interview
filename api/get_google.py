import requests as requests

response = requests.get('https://google.com')

print(response.content)

