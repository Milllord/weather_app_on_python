from threading import *
import open_weather_map

def get_weather(lon, lat):
    t1 = Thread(target=open_weather_map.get_open_weather_map_weather, args=(lon, lat))
    t1.start()
    t1.join()
    # t2 = Thread(te)