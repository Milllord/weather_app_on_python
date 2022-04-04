import json

def create_url(city):
    json_key_open_weather = "Open_Weather_Map_API_key"

    city_name = city

    limit = 1

    with open("api_keys.json") as f:
        d = json.load(f)
        API_key = d[json_key_open_weather]
        print(d)

    url = f"http://api.openweathermap.org/geo/1.0/direct?q=\
    {city_name},&limit={limit}&appid={API_key}"
    print(url)