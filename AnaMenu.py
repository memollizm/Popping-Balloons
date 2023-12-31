from tkinter import Button, Label, font
from tkinter import *


from IPython.terminal.pt_inputhooks import tk
from Oyun import Oyun

from gpt import  *
#from Oyun import *
from Arayuz import Arayuz
from Oyun import Oyun

#from Magaza import *
#from MeydanOkuma import * 

class AnaMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ana Menü")
        self.root.geometry("800x600")

        self.root.configure(bg="#ffbf28")
        self.title_label = Label(self.root, text="Hoşgeldiniz", font=("Helvetica", 20, "bold"), bg="#ffbf28")

        #self.title_label = Label(self.root, text="Hoşgeldiniz", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        self.oyna_button = Button(self.root, text="Oyna", command=self.start_game, width=20, height=2, font=("Arial", 13, "bold"), bg = "#e8e8e8", fg = "black")
        self.meydan_okuma_button = Button(self.root, text="Meydan Okuma", command=self.open_meydan_okuma, width=20, height=2, font=("Arial", 13, "bold"), bg = "#e8e8e8", fg = "black")
        self.magaza_button = Button(self.root, text="Mağaza", command=self.open_magaza, width=20, height=2, font=("Arial", 13, "bold"), bg = "#e8e8e8", fg = "black")
        self.cikis_button = Button(self.root, text="Çıkış", command=self.root.quit, width=20, height=2, font=("Arial", 13, "bold"), bg = "#e8e8e8", fg = "black")

        self.oyna_button.pack(pady=30)
        self.meydan_okuma_button.pack(pady=25)
        self.magaza_button.pack(pady=25)
        self.cikis_button.pack(pady=25)

    def build(self):
        self.title_label = tk.Label(self.root, text="Hoşgeldiniz", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        self.oyna_button = tk.Button(self.root, text="Oyna", command=self.start_game)
        self.oyna_button.pack(pady=10)
        

    def start_game(self):
        self.root.destroy()
        self.main_loop()
        oyun = Oyun(800, 600)
        oyun.main_loop()

    def open_meydan_okuma(self):
        self.root.destroy()
        self.main_game_loop()
        meydan_okuma_root = tk.Toplevel(self.root)
        meydan_okuma = meydan_Okuma(meydan_okuma_root, self.start_game, self.show_game_over_screen)


    def open_magaza(self):
        self.root.destroy()
        self.magaza_baslatma()
        magaza_root = tk.Toplevel(self.root)
        magaza = meydan_Okuma(magaza_root)


    def main_loop(self):
        self.root.mainloop()

   
ana_menu = AnaMenu()
ana_menu.main_loop()

