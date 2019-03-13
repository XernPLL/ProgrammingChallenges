import tkinter as tk
import requests
import os
import subprocess

class MainWindow:
    def __init__(self, master):
        master.title("Download Manager")

        #https://i.ytimg.com/vi/O9dR4KXx8GY/maxresdefault.jpg

        desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]),"Desktop")

        label1 = tk.Label(master, text="URL:")
        label1.grid(row = 0, column=0)

        label2 = tk.Label(master, text="Ścieżka zapisu:")
        label2.grid(row=1, column=0)

        self.eurl = tk.Entry(master, width = 50)
        self.eurl.grid(row=0, column=1)

        self.eusc = tk.Entry(master, width=50)
        self.eusc.grid(row=1, column=1)
        self.eusc.insert(0, desktop)


        pobierz = tk.Button(master, text="Pobierz", command=self.pobierz)
        pobierz.grid(row=2,column=1,pady = 2)

        otworz = tk.Button(master, text = "Otwórz lokalizacje", command=self.otworz)
        otworz.grid(row = 3,column=1, pady = 2)


    def pobierz(self):
        try:
            url = self.eurl.get()
            r = requests.get(url, allow_redirects=True)
            filename = url.rsplit("/",1)[1]
            sciezka = self.eusc.get()+"\\"+filename
            with open(sciezka, 'wb') as code:
                code.write(r.content)

        except:
            print("Błedy url")

    def otworz(self):
        subprocess.Popen('explorer "{}"'.format(self.eusc.get()))




root = tk.Tk()
window = MainWindow(root)
root.mainloop()
