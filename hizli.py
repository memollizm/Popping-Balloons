import tkinter as tk
from random import random
from tkinter import Button
import pygame

import oyna

pygame.mixer.init()

normalBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")
siyahBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Breaking glass sound effect (320 kbps).mp3")

def start_game():
    # Oyun için gerekli kodları buraya ekleyebilirsiniz.

    # Ekran boyutu ve başlık
    screen_width, screen_height = 800, 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Popping Balloons")
    # Renkler
    white = (255, 255, 255)

    # Balon özellikleri
    balloon_radius = 30
    balloon_speed = 3
    balloon_color = (0, 206, 119)

    # Oyuncu özellikleri
    player_width, player_height = 50, 50
    player_x = (screen_width - player_width) // 2
    player_y = screen_height - player_height
    player_speed = 5
    player_color = (255, 165, 0)

    # Zıplama özellikleri
    jumping = False
    jump_count = 10

    # Balonların listesi
    balloons = []

    # Özel balonların listesi (Siyah ve pembe balonlar)
    special_balloons = []

    # Puan
    score = 0

    # Patlatılan balon sayısı
    popped_balloons = 0

    # Hız artışı için eşik değer
    speed_increase_threshold = 5

    # Siyah ve pembe balonların puan etkileri
    black_balloon_score = -5
    pink_balloon_score = 10

    main_menu.destroy()


    # Oyunun açılmasını başlatmak için oyun kodlarını çağırabilirsiniz.
    pygame.init()


    # Oyun döngüsü
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Oyuncunun hareketi
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # Zıplama kontrolü
        if not jumping:
            if keys[pygame.K_SPACE]:
                jumping = True
        else:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                player_y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                jumping = False
                jump_count = 10

        # Yeni balon eklenmesi
        if len(balloons) < 5:
            balloon_x = random.randint(0, screen_width - balloon_radius * 2)
            balloon_y = 0
            balloons.append([balloon_x, balloon_y])

        # Özel balonların eklenmesi (Siyah ve pembe)
        oyna.generate_special_balloon()

        # Balonların hızını artırma
        if popped_balloons >= speed_increase_threshold:
            balloon_speed += 0.1
            speed_increase_threshold += 5

        # Balonların hareketi
        for balloon in balloons:
            balloon[1] += balloon_speed
            if balloon[1] > screen_height:
                balloons.remove(balloon)

        # Özel balonların hareketi
        for special_balloon in special_balloons:
            special_balloon[1] += balloon_speed
            if special_balloon[1] > screen_height:
                special_balloons.remove(special_balloon)

        # Balonları patlatma
        for balloon in balloons:
            if (
                    player_x < balloon[0] + balloon_radius
                    and player_x + player_width > balloon[0]
                    and player_y < balloon[1] + balloon_radius
                    and player_y + player_height > balloon[1]
            ):
                balloons.remove(balloon)
                score += 1
                popped_balloons += 1
                normalBalon_sound.play()

        # Özel balonları patlatma ve puan güncelleme
        for special_balloon in special_balloons:
            if (
                    player_x < special_balloon[0] + balloon_radius
                    and player_x + player_width > special_balloon[0]
                    and player_y < special_balloon[1] + balloon_radius
                    and player_y + player_height > special_balloon[1]
            ):
                siyahBalon_sound.play()
                special_balloons.remove(special_balloon)
                if special_balloon[2] == "black":
                    score += black_balloon_score
                elif special_balloon[2] == "pink":
                    score += pink_balloon_score

        # Ekran temizleme
        screen.fill(white)

        # Balonları çizme
        for balloon in balloons:
            pygame.draw.circle(screen, balloon_color, (balloon[0], balloon[1]), balloon_radius)

        # Özel balonları çizme (Siyah ve pembe)
        for special_balloon in special_balloons:
            if special_balloon[2] == "black":
                pygame.draw.circle(screen, (0, 0, 0), (special_balloon[0], special_balloon[1]), balloon_radius)
            elif special_balloon[2] == "pink":
                pygame.draw.circle(screen, (255, 182, 193), (special_balloon[0], special_balloon[1]), balloon_radius)

        # Oyuncuyu çizme
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

        # Puanı gösterme
        font = pygame.font.Font(None, 36)
        text = font.render(f"Puan: {score}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)


def open_leaderboard():
   """ Meydan okuma veya liderlik tablosu için gerekli kodları buraya ekleyebilirsiniz."""

def open_store():
    """# Mağaza için gerekli kodları buraya ekleyebilirsiniz."""

def open_settings():
    """Ayarlar için gerekli kodları buraya ekleyebilirsiniz."""

main_menu = tk.Tk()
main_menu.title("Popping Ballons")
main_menu.geometry("800x600")

title_label = tk.Label(main_menu, text="Hoşgeldin Kullanıcı 1", font=("Helvetica", 20))
title_label.pack(pady=20)

play_button = Button(main_menu, text="Oyna", command=start_game, width=30, height=2, font=("Helvetica", 12))
leaderboard_button = Button(main_menu, text="Meydan Okuma", command=open_leaderboard, width=30, height=2, font=("Helvetica", 12))
store_button = Button(main_menu, text="Mağaza", command=open_store, width=30, height=2, font=("Helvetica", 12))
settings_button = Button(main_menu, text="Ayarlar", command=open_settings, width=30, height=2, font=("Helvetica", 12))

play_button.pack(pady=10)
leaderboard_button.pack(pady=10)
store_button.pack(pady=10)
settings_button.pack(pady=10)

main_menu.mainloop()
