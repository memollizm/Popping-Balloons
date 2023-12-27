import pygame
import random
import tkinter as tk
from tkinter import ttk

from tkinter import Label, Button

from IPython.terminal.pt_inputhooks import tk
"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ana Menü")
        self.root.geometry("800x600")
"""

class MeydanOkuma:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.root.geometry("800x600")
        self.start_game_callback = start_game_callback

        self.title_label = Label(self.root, text="Meydan Okuma", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

        self.back_button = Button(self.root, text="Geri Dön", command=self.go_back, width=20, height=2, font=("Helvetica", 12))
        self.back_button.pack(pady=10)
        self.start_game()
        self.close_menu()
        self.show_game_over_screen()

    def go_back(self):
        self.root.destroy()

# Oyun süreleri
GAME_DURATION_30S = 30
GAME_DURATION_60S = 60

# Pygame başlatma
pygame.init()

# Ekran ölçüleri
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)

# Oyun özellikleri
FPS = 60
BALLOON_SPEED = 5
PLAYER_SPEED = 10
BALLOON_SIZE = 50
PLAYER_SIZE = 50

# Ses efektleri
pop_sound = pygame.mixer.Sound("ses/yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")

# Oyun değişkenleri
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 2 * PLAYER_SIZE
balloon_x = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)
balloon_y = 0  # Balonların yukarıdan başlaması için
score = 0
time_left = 0

# Oyun süresi kontrolü
game_duration = 0

# Oyun döngüsü kontrolü
running = False

# Oyuncunun zıplama kontrolü için değişkenler
is_jumping = False
jump_count = 10

def start_game(duration):
    global player_x, player_y, balloon_x, balloon_y, score, time_left, game_duration, running

    game_duration = duration
    time_left = game_duration

    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 2 * PLAYER_SIZE
    balloon_x = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)
    balloon_y = 0
    score = 0

    running = True

def close_menu():
    root.destroy()

def show_game_over_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Oyun Bitti!", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50))
    pygame.display.flip()
    pygame.time.delay(3000)  # Ekranı 3 saniye boyunca göster

# Tkinter menüsü
root = tk.Tk()
root.title("Balloon Pop Menu")
root.geometry("400x300")

title_label = ttk.Label(root, text="Balloon Pop Game", font=("Helvetica", 20))
title_label.pack(pady=20)

button_frame = ttk.Frame(root)
button_frame.pack(pady=20)

btn_30s = ttk.Button(button_frame, text="Oyun - 30 Saniye", command=lambda: [start_game(GAME_DURATION_30S), close_menu()])
btn_30s.grid(row=0, column=0, padx=10)

btn_60s = ttk.Button(button_frame, text="Oyun - 60 Saniye", command=lambda: [start_game(GAME_DURATION_60S), close_menu()])
btn_60s.grid(row=0, column=1, padx=10)

close_button = ttk.Button(root, text="Kapat", command=close_menu)
close_button.pack(pady=10)

root.mainloop()

# Pygame ekranı
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Balloon Pop")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if running:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
            player_x += PLAYER_SPEED

        if keys[pygame.K_SPACE]:
            is_jumping = True

        if is_jumping:
            if jump_count >= -10:
                neg = 1 if jump_count > 0 else -1
                player_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 10

        balloon_y += BALLOON_SPEED
        if balloon_y > SCREEN_HEIGHT:
            balloon_x = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)
            balloon_y = 0

        # Çarpışma kontrolü
        if (
            player_x - BALLOON_SIZE < balloon_x < player_x + PLAYER_SIZE
            and player_y - BALLOON_SIZE < balloon_y < player_y + PLAYER_SIZE
        ):
            balloon_x = random.randint(0, SCREEN_WIDTH - BALLOON_SIZE)
            balloon_y = 0
            score += 1
            pop_sound.play()

        screen.fill(WHITE)
        pygame.draw.rect(screen, (0, 128, 255), (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
        pygame.draw.circle(screen, (255, 0, 0), (balloon_x, balloon_y), BALLOON_SIZE)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, (0,0,0))
        time_text = font.render(f"Time Left: {int(time_left)}", True, (0,0,0))
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (SCREEN_WIDTH - 200, 10))

        time_left -= 1 / FPS
        if time_left <= 0:
            running = False
            show_game_over_screen()

    pygame.display.flip()
    clock.tick(FPS)
