import random
import pygame
from soundManager import SoundManager
from tkinter import messagebox

# Ses Kontrolü
sound_manager = SoundManager()


class ücüncüSeviye:
    def __init__(self, root, screen_width, screen_height, game_duration):
        self.root = root
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.game_duration = game_duration
        self.start_time = pygame.time.get_ticks() // 1000
        self.mavi_engel_active = False
        self.mavi_engel_start_time = 0

        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Üçüncü Seviye")

        self.color = (0, 128, 128)
        self.balloon_radius = 30
        self.balloon_speed = 3
        self.balloon_color = (255, 192, 0)

        self.mavi_balloon_radius = 30
        self.mavi_balloon_speed = 3
        self.mavi_balloon_color = (0, 0, 255)

        self.player_width, self.player_height = 50, 50
        self.player_x = (screen_width - self.player_width) // 2
        self.player_y = screen_height - self.player_height
        self.player_speed = 5
        self.player_jump = False
        self.jump_count = 10
        self.player_nitro_active = False
        self.nitro_duration = 5  # Nitro süresi (saniye)
        self.nitro_cooldown = 10  # Nitro kullanım aralığı (saniye)
        self.nitro_last_used = -self.nitro_cooldown  # Başlangıçta nitro kullanılmamış

        self.balloons = []
        self.special_balloons = []
        self.mavi_balloons = []

        self.obstacle_width, self.obstacle_height = 50, 50
        self.obstacle_speed = 3
        self.obstacles = []

        self.score = 0
        self.popped_balloons = 0

        self.speed_increase_threshold = 10
        self.balloon_frequency = 50
        self.balloon_frequency_increase = 10
        self.balloon_speed_increase = 0.05

        self.running = True
        self.clock = pygame.time.Clock()

    def generate_special_balloon(self):
        balloon_x = random.randint(0, self.screen_width - self.balloon_radius * 2)
        balloon_y = 0
        if len(self.special_balloons) % 20 == 0:
            self.special_balloons.append([balloon_x, balloon_y, "black"])
        elif len(self.special_balloons) % 20 == 0:
            self.special_balloons.append([balloon_x, balloon_y, "pink"])

    def generate_obstacle(self):
        obstacle_x = random.randint(0, self.screen_width - self.obstacle_width)
        obstacle_y = 0
        self.obstacles.append([obstacle_x, obstacle_y])

    def check_collision(self):
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
                sound_manager.play_normal_balloon_sound()

        for mavi_balloon in self.mavi_balloons:
            if (
                self.player_x < mavi_balloon[0] + self.mavi_balloon_radius
                and self.player_x + self.player_width > mavi_balloon[0]
                and self.player_y < mavi_balloon[1] + self.mavi_balloon_radius
                and self.player_y + self.player_height > mavi_balloon[1]
            ):
                sound_manager.play_ice_sound()
                self.mavi_balloons.remove(mavi_balloon)
                if not self.mavi_engel_active:
                    self.mavi_engel_active = True
                    self.mavi_engel_start_time = pygame.time.get_ticks() // 1000

        for special_balloon in self.special_balloons:
            if (
                self.player_x < special_balloon[0] + self.balloon_radius
                and self.player_x + self.player_width > special_balloon[0]
                and self.player_y < special_balloon[1] + self.balloon_radius
                and self.player_y + self.player_height > special_balloon[1]
            ):
                sound_manager.play_black_balloon_sound()
                self.special_balloons.remove(special_balloon)
                if special_balloon[2] == "black":
                    self.score += -1
                    if not self.mavi_engel_active:
                        self.mavi_engel_active = True
                        self.mavi_engel_start_time = pygame.time.get_ticks() // 1000
                elif special_balloon[2] == "pink":
                    self.score += 10

        for obstacle in self.obstacles:
            if (
                self.player_x < obstacle[0] + self.obstacle_width
                and self.player_x + self.player_width > obstacle[0]
                and self.player_y < obstacle[1] + self.obstacle_height
                and self.player_y + self.player_height > obstacle[1]
            ):
                self.show_game_summary()

    def use_nitro(self):
        current_time = pygame.time.get_ticks() // 1000
        if current_time - self.nitro_last_used > self.nitro_cooldown:
            self.player_speed += 5
            self.balloon_speed += self.balloon_speed_increase
            self.speed_increase_threshold += 0.1
            self.balloon_frequency -= self.balloon_frequency_increase

            self.nitro_last_used = current_time
            self.player_nitro_active = True

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        self.show_main_menu()
                    elif event.key == pygame.K_SPACE and not self.player_jump:
                        self.player_jump = True
                    elif event.key == pygame.K_n:
                        self.use_nitro()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.player_x > 0:
                self.player_x -= self.player_speed
            if keys[pygame.K_RIGHT] and self.player_x < self.screen_width - self.player_width:
                self.player_x += self.player_speed

            if self.player_jump:
                if self.jump_count >= -10:
                    neg = 1
                    if self.jump_count < 0:
                        neg = -1
                    self.player_y -= (self.jump_count ** 2) * 0.5 * neg
                    self.jump_count -= 1
                else:
                    self.player_jump = False
                    self.jump_count = 10

            # Her 10 puanda bir balon hızı ve düşme sıklığı artacak
            if self.score > 0 and self.score % self.speed_increase_threshold == 0:
                self.use_nitro()

            if self.balloon_frequency <= 0:
                self.balloon_frequency = 1

            if len(self.balloons) < 5 and pygame.time.get_ticks() % self.balloon_frequency == 0:
                balloon_x = random.randint(0, self.screen_width - self.balloon_radius * 2)
                balloon_y = 0
                self.balloons.append([balloon_x, balloon_y])

            if len(self.mavi_balloons) < 1 and pygame.time.get_ticks() % 300 == 0:
                mavi_balloon_x = random.randint(0, self.screen_width - self.mavi_balloon_radius * 2)
                mavi_balloon_y = 0
                self.mavi_balloons.append([mavi_balloon_x, mavi_balloon_y])

            if len(self.obstacles) < 3 and pygame.time.get_ticks() % 100 == 0:
                self.generate_obstacle()

            self.generate_special_balloon()

            for balloon in self.balloons:
                balloon[1] += self.balloon_speed
                if balloon[1] > self.screen_height:
                    self.balloons.remove(balloon)

            for mavi_balloon in self.mavi_balloons:
                mavi_balloon[1] += self.mavi_balloon_speed
                if mavi_balloon[1] > self.screen_height:
                    self.mavi_balloons.remove(mavi_balloon)

            for special_balloon in self.special_balloons:
                special_balloon[1] += self.balloon_speed
                if special_balloon[1] > self.screen_height:
                    self.special_balloons.remove(special_balloon)

            for obstacle in self.obstacles:
                obstacle[1] += self.obstacle_speed
                if obstacle[1] > self.screen_height:
                    self.obstacles.remove(obstacle)

            self.check_collision()
            self.check_mavi_engel()

            self.screen.fill(self.color)

            for balloon in self.balloons:
                pygame.draw.circle(self.screen, self.balloon_color, (balloon[0], balloon[1]), self.balloon_radius)

            for mavi_balloon in self.mavi_balloons:
                pygame.draw.circle(self.screen, self.mavi_balloon_color, (mavi_balloon[0], mavi_balloon[1]),
                                   self.mavi_balloon_radius)

            for special_balloon in self.special_balloons:
                if special_balloon[2] == "black":
                    pygame.draw.circle(self.screen, (0, 0, 0), (special_balloon[0], special_balloon[1]),
                                       self.balloon_radius)
                elif special_balloon[2] == "pink":
                    pygame.draw.circle(self.screen, (255, 182, 193), (special_balloon[0], special_balloon[1]),
                                       self.balloon_radius)

            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen, (139, 69, 19),
                                 (obstacle[0], obstacle[1], self.obstacle_width, self.obstacle_height))

            pygame.draw.rect(self.screen, (255, 248, 220),
                             (self.player_x, self.player_y, self.player_width, self.player_height))

            pygame.font.init()
            font = pygame.font.Font(None, 40)
            text = font.render(f"Puan: {self.score}", True, (248, 248, 255))
            self.screen.blit(text, (10, 10))

            # Süreyi kontrol et ve ekrana yazdır
            elapsed_time = (pygame.time.get_ticks() // 1000) - self.start_time
            remaining_time = max(0, self.game_duration - elapsed_time)
            time_text = font.render(f"Süre: {remaining_time}", True, (248, 248, 255))
            self.screen.blit(time_text, (self.screen_width - 120, 10))

            pygame.display.flip()
            self.clock.tick(60)

            # Oyun süresi bittiğinde oyun özetini göster
            if remaining_time <= 0:
                self.show_game_summary()

        pygame.quit()

    def show_main_menu(self):
        # Ana menüyü göstermek için gerekli işlemleri yapabilirsiniz.
        # Örneğin, self.root.destroy() ile mevcut pencereyi kapatıp ana menüyü gösterebilirsiniz.
        pass

    def show_game_summary(self):
        messagebox.showinfo("Oyun Bitti", f"Puanınız: {self.score}")
        self.running = False

    def check_mavi_engel(self):
        if self.mavi_engel_active:
            current_time = pygame.time.get_ticks() // 1000
            if current_time - self.mavi_engel_start_time <= 5:
                self.player_speed = 0
            else:
                self.mavi_engel_active = False
                self.player_speed = 5


if __name__ == "__main__":
    ücüncü_seviye = ücüncüSeviye(None, 800, 600, 30)
    ücüncü_seviye.main_loop()
