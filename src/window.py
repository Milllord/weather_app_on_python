from tkinter import *
from tkinter import ttk
from city_decoder import decode_city, get_cords

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

class Window:
    def get_weather(self):
        # Получаем город
        # self.city = self.entry_city.get()
        # Получаем координаты города и записываем их в json city_decoder.json

        # РАСКОММЕНТИРОВАТЬ СТРОКУ НИЖЕ!
        # decode_city(self.entry_city)

        # Получаем координаты введенного города
        self.lon, self.lat = get_cords()
        print(f"lon = {self.lon}\n lat = {self.lat}")
        # Получаем погоду по open_weather_map
        

    """
    Класс окна программы приложения погоды.
    """
    def __init__(self):
        """
        Конструктор по умолчанию
        Создает окно с константными параметрами
        Из данного файла выше
        """
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
        
    def main_loop(self):
        """
        Главная функция обработки событий
        """
        # Запускаем обработку событий окна
        self.window.mainloop()