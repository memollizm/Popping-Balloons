import tkinter as tk

class Uygulama:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("İki Pencere Örneği")

        # İlk pencere üzerine bir buton ekleyin
        self.buton1 = tk.Button(ana_pencere, text="Diğer Menü", command=self.ikinci_pencereyi_ac)
        self.buton1.pack(pady=20)

    def ikinci_pencereyi_ac(self):
        # İkinci pencereyi oluşturun
        self.ikinci_pencere = tk.Toplevel(self.ana_pencere)
        self.ikinci_pencere.title("İkinci Pencere")
        self.ikinci_pencere.geometry(f"{self.ana_pencere.winfo_width()}x{self.ana_pencere.winfo_height()}+{self.ana_pencere.winfo_x()}+{self.ana_pencere.winfo_y()}")

        # İkinci pencereye bir buton ekleyin
        self.buton2 = tk.Button(self.ikinci_pencere, text="İlk Pencereye Dön", command=self.ilk_pencereye_don)
        self.buton2.pack(pady=20)

        # İlk pencereyi gizle
        self.ana_pencere.iconify()

    def ilk_pencereye_don(self):
        # İlk pencereyi tekrar göster ve ikinci pencereyi kapat
        self.ana_pencere.deiconify()
        self.ikinci_pencere.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    uygulama = Uygulama(root)
    root.mainloop()