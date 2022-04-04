import json, requests

def get_stack_weather_api_key():
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\api_keys.json") as f:
        d = json.load(f)
        json_key_open_weather = "Weather_Stack_API_key"
        API_key = d[json_key_open_weather]
        print(API_key)
    return API_key

# def get_weather_stack_weather(city):
#     YOUR_ACCESS_KEY = get_stack_weather_api_key()
#     url = f"http://api.weatherstack.com/current ? access_key = {YOUR_ACCESS_KEY} & query = {city}"

#     response = requests.get(url)
#     data = response.json()
#     with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\weather_stack.json", "w") as f:
#         json.dump(data, f)