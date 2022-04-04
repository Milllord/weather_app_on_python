import multiprocessing
import open_weather_map


def processed(lon, lat, procs, calc):
    # procs - количество ядер
    # calc - количество операций на ядро
    
    processes = []
    
    # делим вычисления на количество ядер
    for proc in range(procs):
        p = multiprocessing.Process(target=open_weather_map.get_open_weather_map_weather(lon, lat), 
        args=(calc, proc))
        processes.append(p)
        p.start()
    
    # Ждем, пока все ядра 
    # завершат свою работу.
    for p in processes:
        p.join()

def get_weather(lon, lat):
    n_proc = multiprocessing.cpu_count()
    processed(lon, lat, n_proc, calc=1)
    print("Завершено успешно")