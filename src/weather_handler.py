from threading import *
import open_weather_map

def get_weather(lon, lat):
    thread1 = Thread(target=open_weather_map.get_open_weather_map_weather, args=(lon, lat))
    # thread2 = Thread(te)