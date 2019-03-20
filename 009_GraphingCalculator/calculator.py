import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import re
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.style.use('ggplot')

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Graphic Calculator")
        master.geometry("800x600")

        label1 = tk.Label(master, text="Podaj funkcję:")
        label1.place(x=0, y= 0)

        label2 = tk.Label(master, text="f(x)=")
        label2.place(x=0, y= 25)

        self.entry1 = tk.Entry(master, width = 50)
        self.entry1.place(x=30,y=25)

        label3 = tk.Label(master, text="Dolny limit:")
        label3.place(x=0, y=50)

        self.entry3 = tk.Entry(master)
        self.entry3.insert(0, "-100")
        self.entry3.place(x=65, y=50)

        label4 = tk.Label(master, text="Górny limit:")
        label4.place(x=175, y=50)

        self.entry4 = tk.Entry(master)
        self.entry4.insert(0, "100")
        self.entry4.place(x=240, y=50)

        button1 = tk.Button(master, text="Rysuj wykres", command=self.rysuj)
        button1.place(x=5, y = 75)

        self.button2 = tk.Button(master, text="Dodaj na  wykres", command=self.dodaj)
        self.button2.place_forget()

        self.replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            '^': '**',
        }

        self.allowed_words = [
            'x',
            'sin',
            'cos',
            'sqrt',
            'exp',
        ]

        self.wykresy = {}

    def convert(self, string, x):
        funkcja = eval(self.string2func(string))
        print(x.shape)
        if not(type(funkcja) == type(x)):
            nowa = x.copy()
            nowa.fill(funkcja)
            funkcja = nowa
        return funkcja


    def rysuj(self):
        self.numberofplots = 1
        self.wykresy = {}
        self.min = float(self.entry3.get())
        self.max = float(self.entry4.get())
        x = np.linspace(self.min, self.max, 1000)
        funkcja = self.convert(self.entry1.get(), x)
        self.wykresy[self.numberofplots] = [x, funkcja]
        self.draw()
        self.button2.place(x = 100, y = 75)


    def dodaj(self):
        self.numberofplots = self.numberofplots + 1
        x = np.linspace(self.min, self.max, 1000)
        funkcja = self.convert(self.entry1.get(), x)
        self.wykresy[self.numberofplots] = [x, funkcja]
        self.draw()


    def string2func(self, string):
        for word in re.findall('[a-zA-Z_]+', string):
            if word not in self.allowed_words:
                raise ValueError(
                    messagebox.showerror(
                        "Error", '"{}" is forbidden to use in math expression'.format(word)))
        for old, new in self.replacements.items():
            string = string.replace(old, new)

        return string

    def draw(self):

        fig = Figure(figsize=(5,5), dpi=100)
        self.a = fig.add_subplot(111)
        for key, value in self.wykresy.items():
            self.a.plot(value[0], value[1])
        self.canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.get_tk_widget().place(x = 250, y = 80)
        self.canvas.draw()



root = tk.Tk()
window = MainWindow(root)
root.mainloop()