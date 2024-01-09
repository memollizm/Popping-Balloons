import tkinter as tk
from tkinter import Label, messagebox
import random

class BalanceObserver:
    def update_balance(self, new_balance):
        pass

class Wallet:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount

class StorePage(tk.Frame, BalanceObserver):
    def __init__(self, master, wallet, store_items):
        self.master = master
        self.wallet = wallet
        self.store_items = store_items
        self.observers = []

        self.create_widgets()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update_balance(self.wallet.get_balance())

    def update_balance(self, new_balance):
        self.wallet.update_balance(new_balance)
        self.balance_label.config(text=f"Bakiye: {self.wallet.get_balance()}")
        self.notify_observers()

    def create_widgets(self):
        self.balance_label = Label(self.master, text=f"Bakiye: {self.wallet.get_balance()}", font=("Arial", 14, "bold"), bg="#008080", width=15, height=3)
        self.balance_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        rows, columns = 3, 3

        # Renk paleti
        color_palette = ["#06BEE1", "#06BEE3", "#06BEE6", "#06BEE7", "#06BEE8", "#06BEE9", "#FF5733", "#FFD700", "#8A2BE2"]
        random.shuffle(color_palette)  # Renk paletini karıştır

        used_colors = set()

        for row in range(1, rows + 1):
            for column in range(columns):
                item_name, item_info = f"Nesne {row * columns + column + 1}", (20 + (row * columns + column + 1) * 10, (row * columns + column + 1) % 3 + 1)
                item_price, difficulty = item_info

                # Renk paletinden bir renk al
                color = color_palette.pop(0)
                used_colors.add(color)

                item_button = tk.Button(self.master, text=f"{item_price} Puan", command=lambda price=item_price, clr=color: self.buy_item(price, difficulty, clr), bg=color, width=10, height=3)
                item_button.grid(row=row, column=column, padx=5, pady=5, sticky="w")

    def buy_item(self, item_price, difficulty, color):
        if self.wallet.get_balance() >= item_price:
            self.wallet.update_balance(-item_price)
            self.balance_label.config(text=f"Bakiye: {self.wallet.get_balance()}")
            
            self.master.configure(bg=color)
            
            difficulty_level = "Kolay" if difficulty == 1 else ("Orta" if difficulty == 2 else "Zor")
            success_message = f"BAŞARIYLA SATIN ALINDI! \n"\
                              f"SATIN ALINAN NESNENİN PUANI: {item_price}\n"\
                              f"ZORLUK SEVİYESİ: {difficulty_level}\n"\
                              f"KALAN BAKİYE: {self.wallet.get_balance()}"
            messagebox.showinfo("BAŞARI", success_message)
        else:
            messagebox.showerror("HATA", "YETERSİZ BAKİYE! DAHA FAZLA PUAN KAZANIN...")

def run_store():
    root = tk.Tk()
    root.title("Mağaza")
    root.geometry("800x600")
    root.configure(bg="#008080")

    user_wallet = Wallet(initial_balance=16000)

    store_items = {
        "Nesne 1": (20, 1),
        "Nesne 2": (30, 2),
        "Nesne 3": (15, 3)
    }

    store_page = StorePage(root, user_wallet, store_items)

    root.resizable(False, False)

    root.mainloop()

if __name__ == "__main__":
    run_store()



# Gözlemci (Observer) tasarım deseni kullaılmıştır. 
# Kullanıcının cüzdan bakiyesindeki herhangi bir değişikliği takip etmek isteyen nesneleri (gözlemcileri) mağaza sayfasına eklemek ve bu değişiklikleri anında almak için kullanılır.

from AnaMenu import *
def show_main_menu(self):
    pygame.quit  # Oyun döngüsünü durdur
    self.root.destroy()  # Tkinter penceresini kapat
    ana_menu = AnaMenu()
    ana_menu.build()  # Ana menüyü göster
