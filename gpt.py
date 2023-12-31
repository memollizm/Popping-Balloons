import pygame
import tkinter as tk
from tkinter import Button, Label




class meydan_Okuma:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback

        self.title_label = Label(self.root, text="Meydan Okuma", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        pygame.mixer.init()
        self.normalBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")
        self.siyahBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Breaking glass sound effect (320 kbps).mp3")

        self.back_button = Button(self.root, text="Geri Dön", command=self.go_back, width=20, height=2, font=("Helvetica", 12))
        self.back_button.pack(pady=10)

    def go_back(self):
        self.root.destroy()

class Magaza:
    def __init__(self, root):
        self.root = root

        self.title_label = Label(self.root, text="Mağaza", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        self.back_button = Button(self.root, text="Geri Dön", command=self.go_back, width=20, height=2, font=("Helvetica", 12))
        self.back_button.pack(pady=10)

    def go_back(self):
        self.root.destroy()

