import json
import requests

# Получаем погоду из open_weather_map.org

def get_open_weather_map_weather(lon, lat):
    """
    Функция получения погоды из open_weather_map
    filename - имя файла для записи результата
    lon - широта
    lat - долгота
    """
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\api_keys.json") as f:
        d = json.load(f)
        json_key_open_weather = "Open_Weather_Map_API_key"
        API_key = d[json_key_open_weather]

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

    response = requests.get(url)
    data = response.json()
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\open_weather_map.json", "w") as f:
        json.dump(data, f)