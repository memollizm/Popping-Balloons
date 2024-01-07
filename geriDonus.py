#Anamenu.py
"""
import tkinter as tk
import Oyun

def oyunu_baslat():
    Oyun.main_loop()

root = tk.Tk()
root.geometry('800x600')

oyna_button = tk.Button(root, text="Oyna", command=oyunu_baslat)
oyna_button.pack()

root.mainloop()
"""

#Oyun.py
"""
import tkinter as tk

def oyunu_baslat():
    oyun_penceresi = tk.Toplevel()
    oyun_penceresi.geometry('800x600')

    def oyunu_kapat(event):
        oyun_penceresi.destroy()

    oyun_penceresi.bind('<Escape>', oyunu_kapat)
"""