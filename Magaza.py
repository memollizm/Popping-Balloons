import tkinter as tk
from tkinter import Button, Label, messagebox

# Global oyuncu bakiyesi
player_balance = 100  # Örnek olarak başlangıç bakiyesi

class Magaza:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.title_label = Label(self.root, text="Mağaza", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        self.back_button = Button(self.root, text="Geri Dön", command=self.go_back, width=20, height=2, font=("Helvetica", 12))
        self.back_button.pack(pady=10)

    def go_back(self):
        self.root.destroy()

def open_store():
     store_window = tk.Toplevel(main_menu)
     store_window.title("Mağaza")
     store_window.geometry("400x200")

     # Bakiye etiketi
     balance_label = Label(store_window, text=f"Oyuncu Bakiyesi: {player_balance}", font=("Helvetica", 14))
     balance_label.pack(pady=10)

     # Altın balon satın alma düğmesi
     buy_gold_balloon_button = Button(store_window, text="Altın Satın Al (50 Puan)", command=buy_gold_balloon)
     buy_gold_balloon_button.pack(pady=5)

     # Güçlendirme satın alma düğmesi
     buy_power_up_button = Button(store_window, text="Güçlendirme Satın Al (30 Puan)", command=buy_power_up)
     buy_power_up_button.pack(pady=5)

def buy_gold_balloon():
    global player_balance
    gold_balloon_price = 50  # Altın balon fiyatı (örnek olarak)

    if player_balance >= gold_balloon_price:
        player_balance -= gold_balloon_price
        # Altın balonu envantere eklemek için gerekli kodları buraya ekleyebilirsiniz.
        show_confirmation_message("Altın satın alındı!")
    else:
        show_error_message("Yetersiz bakiye! Altın satın almak için daha fazla puan kazanın")

def buy_power_up():
    global player_balance
    power_up_price = 30  # Güçlendirme fiyatı (örnek olarak)

    if player_balance >= power_up_price:
        player_balance -= power_up_price
        # Güçlendirmeyi uygulamak veya envantere eklemek için gerekli kodları buraya ekleyebilirsiniz.
        show_confirmation_message("Güçlendirme satın alındı!")
    else:
        show_error_message("Yetersiz bakiye! Güçlendirme satın almak için daha fazla puan kazanın")

def show_confirmation_message(message):
    messagebox.showinfo("Onay", message)

def show_error_message(message):
    messagebox.showerror("Hata", message)

# Ana menü oluşturma
main_menu = tk.Tk()
main_menu.title("Popping Balloons")
main_menu.geometry("800x600")

# Mağaza düğmesi
store_button = Button(main_menu, text="Mağaza", command=open_store, width=30, height=2, font=("Helvetica", 12))
store_button.pack(pady=10)

#Ana menüyü başlatma
main_menu.mainloop()
