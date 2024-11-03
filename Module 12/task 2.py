import requests
import json

lat = 60
lon = 21
API_key = "29aa75f05e52bedc66ae97242689d7d9"

request = f"https://api.openweathermap.org/data/2.5/weather?units=metric&lat={lat}&lon={lon}&appid={API_key}"

try:
    response = requests.get(request)
    if not response.ok:
        raise requests.exceptions.RequestsWarning()

    weather = response.json()

    print(f"""
    Location: {weather['name']}
    Temperature: {weather['main']['temp']} degrees
    """)

except requests.exceptions.RequestException as error:
    print('Request could not be completed.')
except requests.exceptions.RequestsWarning as error:
    print('Invalid request')
