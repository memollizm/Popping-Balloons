#Template Method Pattern (Şablona Dayalı Metot Deseni)

import tkinter as tk

class Arayuz:
    def __init__(self, root):
        self.root = root
        self.root.title("Ana Menü")
        self.root.geometry("800x600")

        self.build()

    def build(self):
        raise NotImplementedError("build metodunu alt sınıflarda implemente etmelisiniz.")