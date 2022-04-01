from tkinter import *
from tkinter import ttk

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
        city = StringVar()
        self.entry_city = Entry(self.window, fg="white", bg="gray22", 
        font="Arial 14", width=50, textvariable=city)
        self.entry_city.pack()
        # Создаем стиль tkinter, передав в параметре окно
        self.style = ttk.Style(self.window)
        # Конфигурируем вкладки так, чтобы они отображались слева
        self.style.configure('lefttab.TNotebook', tabposition='ws')
        # Создаем "записную книжку" tkinter с вкладками слева
        self.notebook = ttk.Notebook(self.window, style='lefttab.TNotebook')
    def main_loop(self):
        """
        Главная функция обработки событий
        """
        # Запускаем обработку событий окна
        self.window.mainloop()