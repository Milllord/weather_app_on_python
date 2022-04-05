from threading import *
import open_weather_map
import weather_bit

def get_weather(lon, lat):
    # Создаем потоки
    t1 = Thread(target=open_weather_map.get_open_weather_map_weather(lon, lat))
    t2 = Thread(target=weather_bit.get_weather(lon, lat))
    
    # Запускаем работу
    t1.start()
    t2.start()
   