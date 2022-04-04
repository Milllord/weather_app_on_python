from threading import *
import open_weather_map
import yandex

def get_weather(lon, lat):
    # Создаем потоки
    # t1 = Thread(target=open_weather_map.get_open_weather_map_weather, args=(lon, lat))
    t2 = Thread(target=yandex.get_weather_from_yandex_weather, args=(lon, lat))
    
    # Запускаем работу
    # t1.start()
    t2.start()
    pass
   