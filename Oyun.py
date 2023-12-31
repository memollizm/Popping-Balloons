import random
from tkinter import Button, Tk
import tkinter as tk
import pygame

#pygame.mixer.init()

class Oyun:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Popping Balloons")
        

        self.color = (0, 128, 128)
        self.balloon_radius = 30
        self.balloon_speed = 3
        self.balloon_color = (255, 192, 0,)

        self.player_width, self.player_height = 50, 50
        self.player_x = (screen_width - self.player_width) // 2
        self.player_y = screen_height - self.player_height
        self.player_speed = 5
        self.player_speed = self.balloon_speed * 2
        self.player_color = (255, 248, 220)

        self.jumping = False
        self.jump_count = 10

        self.balloons = []
        self.special_balloons = []

        self.score = 0
        self.popped_balloons = 0

        self.speed_increase_threshold = 5

        pygame.mixer.init()
        self.normalBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")
        self.siyahBalon_sound = pygame.mixer.Sound("ses/yt5s.io - Breaking glass sound effect (320 kbps).mp3")
        

        self.running = True
        self.clock = pygame.time.Clock()

        
        #------------GERİ DÖNÜŞ BUTON-------------------------------------------------------------------------------------------------------------
        #self.geriDonus = tk.Button(self, text="Geri", command = ana_menuye_don)
        #self.geriDonus.pack(pady = 20)

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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Kullanıcı Escape tuşuna bastığında
                        self.running = False
                        self.show_main_menu()

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

            self.screen.fill(self.color)

            for balloon in self.balloons:
                pygame.draw.circle(self.screen, self.balloon_color, (balloon[0], balloon[1]), self.balloon_radius)

            for special_balloon in self.special_balloons:
                if special_balloon[2] == "black":
                    pygame.draw.circle(self.screen, (0, 0, 0), (special_balloon[0], special_balloon[1]), self.balloon_radius)
                elif special_balloon[2] == "pink":
                    pygame.draw.circle(self.screen, (255, 182, 193), (special_balloon[0], special_balloon[1]), self.balloon_radius)

            pygame.draw.rect(self.screen, self.player_color, (self.player_x, self.player_y, self.player_width, self.player_height))

            pygame.font.init()
            font = pygame.font.Font(None, 40)
            text = font.render(f"Puan: {self.score}", True, (248, 248, 255))
            self.screen.blit(text, (10, 10))
            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

"""   
def show_main_menu():
     self.root.destroy()  # Oyun penceresini kapat
     self.root.deiconify()  # Ana menü penceresini tekrar göster
     self.root.withdraw()  # Oyun penceresini gizle
     ana_menu = AnaMenu(self.root)


if __name__ == "__main__":
ana_menu = AnaMenu()
ana_menu.root.mainloop()

def go_back(self):
    self.root.destroy()
"""
    

