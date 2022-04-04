import json
import requests

def decode_city(city):
    json_key_open_weather = "Open_Weather_Map_API_key"

    city_name = city

    limit = 1

    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\api_keys.json") as f:
        d = json.load(f)
        API_key = d[json_key_open_weather]

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},&limit={limit}&appid={API_key}"
    
    response = requests.get(url)
    data = response.json()
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\city_decoder.json", "w") as f:
        json.dump(data, f)

def get_cords():
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\city_decoder.json", "r") as f:
        d = json.load(f)
        return d[0]["lon"], d[0]["lat"]