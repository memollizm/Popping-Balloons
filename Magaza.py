import tkinter as tk
from tkinter import Button, Label, messagebox
from Oyun import *

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
     # Bakiye kutusunu üstte oluştur
     self.balance_label = Label(self.master, text=f"Bakiye: {self.wallet.get_balance()}", font=("Arial", 14, "bold"), bg="#008080", width=15, height=3)
     self.balance_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

     # Renk paleti
     color_palette = ["#06BEE1", "#06BEE3", "#06BEE6", "#06BEE7", "#06BEE8", "#06BEE9"]

     # Mağaza nesnelerini sırala
     row_counter = 1
     sorted_items = sorted(self.store_items.items(), key=lambda x: x[1][1])

     for (item_name, item_info), color in zip(sorted_items, color_palette):
         item_price, difficulty = item_info

         item_button = tk.Button(self.master, text=f"{item_price} Puan", command=lambda price=item_price: self.buy_item(price, difficulty), bg=color, width=10, height=3)
         item_button.grid(row=row_counter, column=0, padx=5, pady=5, sticky="w")
         row_counter += 1

     # Daha fazla nesne butonları
     more_items = {
         "Nesne 4": (150, 2),
         "Nesne 5": (180, 2),
         "Nesne 6": (250, 2),
         "Nesne 7": (300, 3),
         "Nesne 8": (370, 3),
         "Nesne 9": (500, 3)
     }

     column_counter = 1
     for (item_name, item_info), color in zip(more_items.items(), color_palette):
         item_price, difficulty = item_info

         item_button = tk.Button(self.master, text=f"{item_price} Puan", command=lambda price=item_price: self.buy_item(price, difficulty), bg=color, width=10, height=3)
         item_button.grid(row=row_counter, column=column_counter, padx=5, pady=5, sticky="w")
         column_counter += 1
         if column_counter == 3:
             column_counter = 1
             row_counter += 1

    def buy_item(self, item_price, difficulty):
        if self.wallet.get_balance() >= item_price:
            self.wallet.update_balance(-item_price)
            self.balance_label.config(text=f"Bakiye: {self.wallet.get_balance()}")

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

    # Cüzdanı oluştur
    user_wallet = Wallet(initial_balance=score)

    # Mağaza nesnelerini belirle (örnek olarak)
    store_items = {
        "Nesne 1": (20, 1),
        "Nesne 2": (30, 2),
        "Nesne 3": (15, 3)
    }

    # Mağaza sayfasını oluştur
    store_page = StorePage(root, user_wallet, store_items)

    # Pencereyi sabitle
    root.resizable(False, False)

    root.mainloop()

if __name__ == "__main__":
    run_store()

# Gözlemci (Observer) tasarım deseni kullaılmıştır. 
# Kullanıcının cüzdan bakiyesindeki herhangi bir değişikliği takip etmek isteyen nesneleri (gözlemcileri) mağaza sayfasına eklemek ve bu değişiklikleri anında almak için kullanılır.

def main_loop(self):
    while self.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.show_main_menu()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.show_main_menu()

        pygame.display.flip()
        self.clock.tick(60)

    pygame.quit()


from AnaMenu import *
def show_main_menu(self):
    pygame.quit  # Oyun döngüsünü durdur
    self.root.destroy()  # Tkinter penceresini kapat
    ana_menu = AnaMenu()
    ana_menu.build()  # Ana menüyü göster
