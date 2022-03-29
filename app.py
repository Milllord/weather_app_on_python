from window import Window

class Application:
    """
    Класс приложения почты.
    """
    def __init__(self):
        # Создаем экземпляр класса окна
        self.window = Window()
    def run(self):
        # Запуск приложения
        self.window.main_loop()