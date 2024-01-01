import tkinter as tk
from tkinter import Button, Label, messagebox

class StorePage:
    def __init__(self, master, user_balance, store_items):
        self.master = master
        self.user_balance = user_balance
        self.store_items = store_items

        self.create_widgets()

    def create_widgets(self):
        # Bakiye kutusunu üstte oluştur
        self.balance_label = Label(self.master, text=f"Bakiye: {self.user_balance}", font=("Helvetica", 14), width=15, height=3)
        self.balance_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Renk paleti
        color_palette = ["#FF5733", "#FFD700", "#33FF57", "#3399FF", "#9966FF", "#FF33FF"]

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
            "Nesne 4": (25, 2),
            "Nesne 5": (40, 3),
            "Nesne 6": (15, 1)
        }

        for (item_name, item_info), color in zip(more_items.items(), color_palette):
            item_price, difficulty = item_info

            item_button = tk.Button(self.master, text=f"{item_price} Puan", command=lambda price=item_price: self.buy_item(price, difficulty), bg=color, width=10, height=3)
            item_button.grid(row=row_counter, column=0, padx=5, pady=5, sticky="w")
            row_counter += 1

    def buy_item(self, item_price, difficulty):
        if self.user_balance >= item_price:
            self.user_balance -= item_price
            self.balance_label.config(text=f"Bakiye: {self.user_balance}")

            difficulty_level = "Kolay" if difficulty == 1 else ("Orta" if difficulty == 2 else "Zor")
            success_message = f"BAŞARIYLA SATIN ALINDI! \n"\
                              f"SATIN ALINAN NESNENİN PUANI: {item_price}\n"\
                              f"ZORLUK SEVİYESİ: {difficulty_level}\n"\
                              f"KALAN BAKİYE: {self.user_balance}"

            messagebox.showinfo("BAŞARI", success_message)
        else:
            messagebox.showerror("HATA", "YETERSİZ BAKİYE! DAHA FAZLA PUAN KAZANIN...")

def main():
    root = tk.Tk()
    root.title("MAĞAZA")
    root.geometry("600x500")

    # Mağaza nesnelerini belirle (örnek olarak)
    store_items = {
        "Nesne 1": (20, 1),
        "Nesne 2": (30, 2),
        "Nesne 3": (15, 3)
    }

    # Kullanıcı bakiyesini belirle
    user_balance = 100

    # Mağaza sayfasını oluştur
    store_page = StorePage(root, user_balance, store_items)

    # Pencereyi sabitle
    root.resizable(False, False)

    root.mainloop()

if __name__ == "__main__":
    main()
