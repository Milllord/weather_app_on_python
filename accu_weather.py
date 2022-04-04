import json, requests

def get_accu_weather_api_key():
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\api_keys.json") as f:
        d = json.load(f)
        json_key_open_weather = "Accu_Weather_API_key"
        API_key = d[json_key_open_weather]
    return API_key

def get_weather_from_yandex_weather(lon, lat):
    lang = "en_US"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    API_Key =  get_accu_weather_api_key()
    url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&[lang={lang}]X-Yandex-API-Key:{API_Key}"
    response = requests.get(url)
    data = response.json()
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\.json", "w") as f:
        json.dump(data, f)