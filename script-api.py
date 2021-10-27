import requests

key = '810f7ab17a074a5bbb6ce92f9ea3eb7a'
units = 'metric'
cidade = 'pirapora'
url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&units={units}&appid={key}'

response = requests.get(url)

temp = response.json()['main']['temp']
cidade = response.json()['name']
print(cidade)
print(temp)
