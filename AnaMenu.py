from tkinter import Button, Label

from IPython.terminal.pt_inputhooks import tk

from gpt import Magaza, MeydanOkuma, Oyun


class AnaMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ana Menü")
        self.root.geometry("800x600")

        self.title_label = Label(self.root, text="Hoşgeldiniz", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        self.oyna_button = Button(self.root, text="Oyna", command=self.start_game, width=20, height=2, font=("Helvetica", 12))
        self.meydan_okuma_button = Button(self.root, text="Meydan Okuma", command=self.open_meydan_okuma, width=20, height=2, font=("Helvetica", 12))
        self.magaza_button = Button(self.root, text="Mağaza", command=self.open_magaza, width=20, height=2, font=("Helvetica", 12))
        self.cikis_button = Button(self.root, text="Çıkış", command=self.root.quit, width=20, height=2, font=("Helvetica", 12))

        self.oyna_button.pack(pady=10)
        self.meydan_okuma_button.pack(pady=10)
        self.magaza_button.pack(pady=10)
        self.cikis_button.pack(pady=10)

    def start_game(self):
        self.root.destroy()
        oyun = Oyun(800, 600)
        oyun.main_loop()

    def open_meydan_okuma(self):
        self.root.destroy()
        meydan_okuma_root = tk.Toplevel(self.root)
        meydan_okuma = MeydanOkuma(meydan_okuma_root, self.start_game, self.show_game_over_screen)


    def open_magaza(self):
        self.root.destroy()
        magaza_root = tk.Toplevel(self.root)
        magaza = Magaza(magaza_root)


    def main_loop(self):
        self.root.mainloop()
