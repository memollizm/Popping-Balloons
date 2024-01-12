import tkinter as tk
from tkinter import messagebox

import pygame
from BirinciSeviye import BirinciSeviye 
from ikinciSeviye import IkinciSeviye
from ucuncuSeviye import ücüncüSeviye

class SeviyeStratejisi:
    def __init__(self, root, screen_width, screen_height, game_duration):
        self.root = root
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_duration = game_duration

    def baslat(self):
        raise NotImplementedError("Alt sınıflar bu metodu uygulamalıdır.")

class BirinciSeviyeStratejisi(SeviyeStratejisi):
    def baslat(self):
        birinci_seviye = BirinciSeviye(self.root, screen_width=self.screen_width, screen_height=self.screen_height, game_duration=self.game_duration)
        birinci_seviye.main_loop()

class IkinciSeviyeStratejisi(SeviyeStratejisi):
    def baslat(self):
        ikinci_seviye = IkinciSeviye(self.root, screen_width=self.screen_width, screen_height=self.screen_height, game_duration=self.game_duration)
        ikinci_seviye.main_loop()

class UcuncuSeviyeStratejisi(SeviyeStratejisi):
    def baslat(self):
        ucuncu_seviye = ücüncüSeviye(self.root, screen_width=self.screen_width, screen_height=self.screen_height, game_duration=self.game_duration)
        ucuncu_seviye.main_loop()

class MeydanOkumaMenu:
    def __init__(self, screen_width, screen_height, game_duration): 
        self.root = tk.Tk()
        self.root.title("Meydan Okuma Menüsü")
        self.root.geometry(f"{screen_width}x{screen_height}")

        self.label = tk.Label(self.root, text="Meydan Okuma Menüsü", font=("Arial", 20, "bold"), bg="#ffbf28")
        self.label.pack(pady=20)

        self.game_duration = game_duration  
        self.seviye_stratejisi = None

        self.root.configure(bg="#ffbf28")

        self.seviye_secim_ekrani()

    def seviye_secim_ekrani(self):
        label = tk.Label(self.root, text="Seviye Seçimi", font=("Arial", 15, "bold "), bg="#ffbf28")
        label.pack(pady=20)

        seviye_frame = tk.Frame(self.root)
        seviye_frame.pack(pady=10)

        for seviye in range(1, 4):
            buton = tk.Button(seviye_frame, text=f"Seviye {seviye}", command=lambda sev=seviye: self.seviye_secildi(sev),
                  borderwidth=2, relief="solid", font=("Arial", 12, "bold"), width=10, height=2, bg="#008080", fg="#ffbf28")

            buton.grid(row=0, column=seviye-1, padx=10)

    def seviye_secildi(self, secilen_seviye):
        messagebox.showinfo("Seviye Seçimi", f"Seviye {secilen_seviye} seçildi.")

        if secilen_seviye == 1:
            self.seviye_stratejisi = BirinciSeviyeStratejisi(self.root, screen_width=800, screen_height=600, game_duration=40)
        elif secilen_seviye == 2:
            self.seviye_stratejisi = IkinciSeviyeStratejisi(self.root, screen_width=800, screen_height=600,game_duration=40)
        elif secilen_seviye == 3:
            self.seviye_stratejisi = UcuncuSeviyeStratejisi(self.root, screen_width=800, screen_height=600,game_duration=40)

        if self.seviye_stratejisi:
            self.seviye_stratejisi.baslat()

if __name__ == "__main__":
    meydan_okuma_menu = MeydanOkumaMenu(800, 600, 400)  
    meydan_okuma_menu.root.mainloop()
