import pygame
import random
import tkinter as tk
from tkinter import Button, Label

class MeydanOkuma:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback

        self.title_label = Label(self.root, text="Meydan Okuma", font=("Helvetica", 20))
        self.title_label.pack(pady=20)

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

class Oyun:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Popping Balloons")

        self.white = (255, 255, 255)
        self.balloon_radius = 30
        self.balloon_speed = 3
        self.balloon_color = (0, 206, 119)

        self.player_width, self.player_height = 50, 50
        self.player_x = (screen_width - self.player_width) // 2
        self.player_y = screen_height - self.player_height
        self.player_speed = 5
        self.player_speed = self.balloon_speed * 2
        self.player_color = (255, 165, 0)

        self.jumping = False
        self.jump_count = 10

        self.balloons = []
        self.special_balloons = []

        self.score = 0
        self.popped_balloons = 0

        self.speed_increase_threshold = 5

        """
        self.normalBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")
        self.siyahBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Breaking glass sound effect (320 kbps).mp3")
        """

        self.running = True
        self.clock = pygame.time.Clock()

    def generate_special_balloon(self):
        balloon_x = random.randint(0, self.screen_width - self.balloon_radius * 2)
        balloon_y = 0
        if len(self.special_balloons) % 30 == 0:
            self.special_balloons.append([balloon_x, balloon_y, "black"])
        elif len(self.special_balloons) % 20 == 0:
            self.special_balloons.append([balloon_x, balloon_y, "pink"])

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_x > 0:
                self.player_x -= self.player_speed
            if keys[pygame.K_RIGHT] and self.player_x < self.screen_width - self.player_width:
                self.player_x += self.player_speed

            if not self.jumping:
                if keys[pygame.K_SPACE]:
                    self.jumping = True
            else:
                if self.jump_count >= -10:
                    neg = 1
                    if self.jump_count < 0:
                        neg = -1
                    self.player_y -= (self.jump_count ** 2) * 0.5 * neg
                    self.jump_count -= 1
                else:
                    self.jumping = False
                    self.jump_count = 10

            if len(self.balloons) < 5:
                balloon_x = random.randint(0, self.screen_width - self.balloon_radius * 2)
                balloon_y = 0
                self.balloons.append([balloon_x, balloon_y])

            self.generate_special_balloon()

            if self.popped_balloons >= self.speed_increase_threshold:
                self.balloon_speed += 0.1
                self.speed_increase_threshold += 5

            for balloon in self.balloons:
                balloon[1] += self.balloon_speed
                if balloon[1] > self.screen_height:
                    self.balloons.remove(balloon)

            for special_balloon in self.special_balloons:
                special_balloon[1] += self.balloon_speed
                if special_balloon[1] > self.screen_height:
                    self.special_balloons.remove(special_balloon)

            for balloon in self.balloons:
                if (
                    self.player_x < balloon[0] + self.balloon_radius
                    and self.player_x + self.player_width > balloon[0]
                    and self.player_y < balloon[1] + self.balloon_radius
                    and self.player_y + self.player_height > balloon[1]
                ):
                    self.balloons.remove(balloon)
                    self.score += 1
                    self.popped_balloons += 1
                    self.normalBalon_sound.play()

            for special_balloon in self.special_balloons:
                if (
                    self.player_x < special_balloon[0] + self.balloon_radius
                    and self.player_x + self.player_width > special_balloon[0]
                    and self.player_y < special_balloon[1] + self.balloon_radius
                    and self.player_y + self.player_height > special_balloon[1]
                ):
                    self.siyahBalon_sound.play()
                    self.special_balloons.remove(special_balloon)
                    if special_balloon[2] == "black":
                        self.score += -5
                    elif special_balloon[2] == "pink":
                        self.score += 10

            self.screen.fill(self.white)

            for balloon in self.balloons:
                pygame.draw.circle(self.screen, self.balloon_color, (balloon[0], balloon[1]), self.balloon_radius)

            for special_balloon in self.special_balloons:
                if special_balloon[2] == "black":
                    pygame.draw.circle(self.screen, (0, 0, 0), (special_balloon[0], special_balloon[1]), self.balloon_radius)
                elif special_balloon[2] == "pink":
                    pygame.draw.circle(self.screen, (255, 182, 193), (special_balloon[0], special_balloon[1]), self.balloon_radius)

            pygame.draw.rect(self.screen, self.player_color, (self.player_x, self.player_y, self.player_width, self.player_height))

            font = pygame.font.Font(None, 36)
            text = font.render(f"Puan: {self.score}", True, (0, 0, 0))
            self.screen.blit(text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

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
        meydan_okuma_root = tk.Toplevel(self.root)
        meydan_okuma = MeydanOkuma(meydan_okuma_root, self.start_game)
        MeydanOkuma()
        #meydan_okuma2 = MeydanOkuma(meydan_okuma_root, self.close_menu)
        #meydan_okuma3 = MeydanOkuma(meydan_okuma_root, self.show_game_over_screen)

    def open_magaza(self):
        magaza_root = tk.Toplevel(self.root)
        magaza = Magaza(magaza_root)

    def main_loop(self):
        self.root.mainloop()

# Ana menüyü görüntüle
ana_menu = AnaMenu()
ana_menu.main_loop()
