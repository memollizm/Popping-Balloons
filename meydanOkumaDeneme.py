import pygame
import random
import tkinter as tk
from tkinter import ttk

pygame.mixer.init()
pop_sound = pygame.mixer.Sound("ses\yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")

class Model:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.player_size = 50
        self.balloon_size = 50
        self.balloon_speed = 5
        self.player_speed = 10
        self.fps = 60

        self.player_x = self.screen_width // 2
        self.player_y = self.screen_height - 2 * self.player_size
        self.balloon_x = random.randint(0, self.screen_width - self.balloon_size)
        self.balloon_y = 0
        self.score = 0
        self.time_left = 0
        self.game_duration = 0
        self.running = False

        self.is_jumping = False
        self.jump_count = 10

        self.clock = pygame.time.Clock()

    def start_game(self, duration):
        self.player_x = self.screen_width // 2
        self.player_y = self.screen_height - 2 * self.player_size
        self.balloon_x = random.randint(0, self.screen_width - self.balloon_size)
        self.balloon_y = 0
        self.score = 0
        self.game_duration = duration
        self.time_left = self.game_duration
        self.running = True

    def update(self):
        if self.running:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_x > 0:
                self.player_x -= self.player_speed
            if keys[pygame.K_RIGHT] and self.player_x < self.screen_width - self.player_size:
                self.player_x += self.player_speed

            if keys[pygame.K_SPACE]:
                self.is_jumping = True

            if self.is_jumping:
                if self.jump_count >= -10:
                    neg = 1 if self.jump_count > 0 else -1
                    self.player_y -= (self.jump_count ** 2) * 0.5 * neg
                    self.jump_count -= 1
                else:
                    self.is_jumping = False
                    self.jump_count = 10

            self.balloon_y += self.balloon_speed
            if self.balloon_y > self.screen_height:
                self.balloon_x = random.randint(0, self.screen_width - self.balloon_size)
                self.balloon_y = 0

            if (
                self.player_x - self.balloon_size < self.balloon_x < self.player_x + self.player_size
                and self.player_y - self.balloon_size < self.balloon_y < self.player_y + self.player_size
            ):
                self.balloon_x = random.randint(0, self.screen_width - self.balloon_size)
                self.balloon_y = 0
                self.score += 1
                pygame.mixer.Sound.play(pop_sound)

            self.time_left -= 1 / self.fps
            if self.time_left <= 0:
                self.running = False

class ExtendedModel(Model):  # Alt sınıf örneği
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self.new_attribute = "Extended Model Attribute"

class View:
    def __init__(self, model):
        self.model = model
        pygame.init()
        self.screen = pygame.display.set_mode((self.model.screen_width, self.model.screen_height))
        pygame.display.set_caption("Balloon Pop")

    def show_game_over_screen(self):
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("Oyun Bitti!", True, (255, 0, 0))
        score_text = font.render(f"Score: {self.model.score}", True, (0, 0, 0))
        self.screen.blit(game_over_text, (self.model.screen_width // 2 - 150, self.model.screen_height // 2 - 50))
        self.screen.blit(score_text, (self.model.screen_width // 2 - 100, self.model.screen_height // 2 + 50))
        pygame.display.flip()
        pygame.time.delay(3000)

    def draw(self):
        self.screen.fill((255, 255, 255))
        pygame.draw.rect(self.screen, (0, 128, 255), (self.model.player_x, self.model.player_y, self.model.player_size, self.model.player_size))
        pygame.draw.circle(self.screen, (255, 0, 0), (self.model.balloon_x, self.model.balloon_y), self.model.balloon_size)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.model.score}", True, (0,0,0))
        time_text = font.render(f"Time Left: {int(self.model.time_left)}", True, (0,0,0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(time_text, (self.model.screen_width - 200, 10))

        pygame.display.flip()

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_game_callback(self, duration, menu_root):
        self.model.start_game(duration)
        menu_root.destroy()

    def close_menu_callback(self, menu_root):
        menu_root.destroy()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.model.update()
            self.view.draw()

            if not self.model.running:
                self.view.show_game_over_screen()
                self.model.running = True  # Restart the game

            self.model.clock.tick(self.model.fps)

if __name__ == "__main__":
    menu_root = tk.Tk()
    menu_root.title("Balloon Pop Menu")
    menu_root.geometry("800x600")

    model = ExtendedModel(800, 600)  # Alt sınıf kullanımı
    view = View(model)
    controller = Controller(model, view)

    title_label = ttk.Label(menu_root, text="Balloon Pop Game", font=("Helvetica", 20))
    title_label.pack(pady=20)

    button_frame = ttk.Frame(menu_root)
    button_frame.pack(pady=20)

    btn_30s = ttk.Button(button_frame, text="Kolay", command=lambda: controller.start_game_callback(30, menu_root))
    btn_30s.grid(row=0, column=0, padx=10)

    btn_60s = ttk.Button(button_frame, text="Zor",command=lambda: controller.start_game_callback(60, menu_root))
    btn_60s.grid(row=0, column=1, padx=10)

    close_button = ttk.Button(menu_root, text="Kapat", command=lambda: controller.close_menu_callback(menu_root))
    close_button.pack(pady=10)

    menu_root.mainloop()

    controller.run()
