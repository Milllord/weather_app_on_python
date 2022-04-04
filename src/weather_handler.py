from threading import *
import open_weather_map
import weather_stack

def get_weather(city, lon, lat):
    # Создаем потоки
    # t1 = Thread(target=open_weather_map.get_open_weather_map_weather, args=(lon, lat))
    t2 = Thread(target=weather_stack.get_weather_stack_weather(city))
    
    # Запускаем работу
    # t1.start()
    t2.start()
    pass
   