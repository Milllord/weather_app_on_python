import json, requests

def get_API_key():
    json_key_open_weather = "Weather_Bit_API_key"
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\api_keys.json") as f:
        d = json.load(f)
        API_key = d[json_key_open_weather]
    return API_key

def get_weather(lon, lat):
    API_Key = get_API_key()
    url = f"https://api.weatherbit.io/v2.0/current?key={API_Key}&lat={lat}&lon={lon}"
    response = requests.get(url)
    data = response.json()
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\weather_bit.json", "w") as f:
        json.dump(data, f)