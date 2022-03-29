from tkinter import *  
from tkinter import ttk  

class TabControl:
    def __init__(self, window):
        self.window = window
        self.tab_control = ttk.Notebook(window)
        tab1 = ttk.Frame(self.tab_control)  
        tab2 = ttk.Frame(self.tab_control)  
        self.tab_control.add(tab1, text='Первая')  
        self.tab_control.add(tab2, text='Вторая')  
        lbl1 = Label(tab1, text='Вкладка 1')  
        lbl1.grid(column=0, row=0)  
        lbl2 = Label(tab2, text='Вкладка 2')  
        lbl2.grid(column=0, row=0)  
        self.tab_control.pack(expand=1, fill='both')  