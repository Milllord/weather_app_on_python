from cgitb import text
from select import select
from tkinter import *
from city_decoder import decode_city, get_cords
from open_weather_map import get_open_weather_map_weather
from weather_handler import get_weather
import json

# Ширина экрана
SCREEN_WIDTH = 1000
# Высота экрана
SCREEN_HIGHT = 600
# Положение окна при создании по оси x
WINDOW_X = 150
# Положение окна при создании по оси y
WINDOW_Y = 50
# Название окна
WINDOW_NAME = "Приложение погоды"

def get_open_weather_map_weather_from_json():
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\open_weather_map.json") as f:
        d = json.load(f)
        humidity = d["main"]["humidity"]
        # Перевод температуры из фаренгейтов в градусы
        temp = int(int(d["main"]["temp"])-273)
        wind_speed = d["wind"]["speed"]
        weather_description = d["weather"][0]["description"]
        return humidity, temp, wind_speed, weather_description
    
def get_weather_bit_weather_from_json():
    with open("C:\\Users\\L0ll1p0p\\AppData\\Local\\GitHubDesktop\\app-2.9.12\\weather_app_on_python\\src\\weather_bit.json") as f:
        d = json.load(f)
        humidity = d["data"][0]["rh"]
        temp = int(d["data"][0]["temp"])
        wind_speed = d["data"][0]["wind_spd"]
        weather_description = d["data"][0]["weather"]["description"]
        return humidity, temp, wind_speed, weather_description

class Window:
    def init_weather(self):
        self.label_weather_provider = Label(text="Open Weather Map", fg="#B0E0E6", bg="gray22", font="Arial 14")
        self.label_weather_provider.pack()
        self.labels_weather = []
        for i in range(len(self.weather_openweather)):
            text1 = ""
            self.labels_weather.append(Label(text=text1, fg="white", bg="gray22", font="Arial 14"))
            self.labels_weather[i].pack()
        self.label_weather_provider1 = Label(text="Weather Bit", fg="#B0E0E6", bg="gray22", font="Arial 14")
        self.label_weather_provider1.pack()
        self.labels_weather1 = []
        for i in range(len(self.weather_openweather)):
            self.labels_weather1.append(Label(text=text1, fg="white", bg="gray22", font="Arial 14"))
            self.labels_weather1[i].pack()

    def show_weather(self):
        for i in range(len(self.weather_openweather)):
            self.labels_weather[i].config(text=(str(self.info[i]) + str(self.weather_openweather[i]) + str(self.units[i])))
        for i in range(len(self.weather_openweather)):
            self.labels_weather1[i].config(text=(str(self.info[i]) + str(self.weather_weatherbit[i]) + str(self.units[i])))

    def get_weather(self):
        # Получаем город
        self.city = self.entry_city.get()
        # Получаем координаты города и записываем их в json city_decoder.json

        # РАСКОММЕНТИРОВАТЬ СТРОКУ НИЖЕ!
        decode_city(self.city)

        # Получаем координаты введенного города
        self.lon, self.lat = get_cords()

        # Получаем погоду
        get_weather(self.lon, self.lat)

        # Влажность, температура в цельсиях, скорость ветра в м/c, описание погоды
        
        self.weather_openweather = get_open_weather_map_weather_from_json()
        self.weather_weatherbit = get_weather_bit_weather_from_json()
        # Отображаем на экране
        self.show_weather()

    """
    Класс окна программы приложения погоды.
    """
    def __init__(self):
        """
        Конструктор по умолчанию
        Создает окно с константными параметрами
        Из данного файла выше
        """
       
        self.init_weather()
        # Создаем окно
        self.window = Tk()
        # Задаем название окна
        self.window.title(WINDOW_NAME)
        # Задаем геометрию окна
        # Будет создано окно размерами:
        # SCREEN_WIDTH x SCREEN_HIGHT
        # С начальным положением:
        # x = WINDOW_X
        # y = WINDOW_Y
        self.window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HIGHT}+{WINDOW_X}+{WINDOW_Y}")
        self.window["bg"] = "gray22"

        # Текст приглашение ко вводу города
        self.label = Label(text="Введите город:", fg="white", bg="gray22", font="Arial 14")
        self.label.pack()
 
        # Создание переменной под город
        self.city = StringVar()

        # Создание поля ввода под погоду
        self.entry_city = Entry(self.window, fg="white", bg="gray22", 
        font="Arial 14", width=50, textvariable=self.city, justify=CENTER)
        
        # Запаковываем на окно
        self.entry_city.pack()

        btn = Button(text="Получить!", background="#555", foreground="#ccc",
             padx="20", pady="8", font="16", command=self.get_weather)
        btn.pack()

         # Получаем необходимые данные
        self.weather_openweather = []
        self.weather_weatherbit = []

        self.info = ["Влажность: ", "Температура: ", "Скорость ветра: ", "Описание погоды: "]
        self.units = [" %", " °C", " м/c", " "]
        
    def main_loop(self):
        """
        Главная функция обработки событий
        """
        # Запускаем обработку событий окна
        self.window.mainloop()