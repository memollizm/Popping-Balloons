import pygame
import random
import sys

class MeydanOkuma:
    def __init__(self, screen_width, screen_height, game_duration):
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Meydan Oku")

        self.color = (0, 128, 128)
        self.balloon_radius = 30
        self.balloon_speed = 3
        self.balloon_color = (255, 192, 0)

        self.player_width, self.player_height = 50, 50
        self.player_x = (screen_width - self.player_width) // 2
        self.player_y = screen_height - self.player_height
        self.player_speed = 5
        self.jumping = False
        self.jump_count = 10

        self.balloons = []
        self.special_balloons = []

        self.score = 0
        self.popped_balloons = 0
        self.black_balloons_popped = 0
        self.pink_balloons_popped = 0

        self.speed_increase_threshold = 5
        self.game_duration = game_duration
        self.sure = game_duration

        pygame.mixer.init()
        self.normalBalon_sound = pygame.mixer.Sound("ses\\yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")
        self.siyahBalon_sound = pygame.mixer.Sound("ses\\yt5s.io - Breaking glass sound effect (320 kbps).mp3")

        self.running = True
        self.clock = pygame.time.Clock()

    def generate_special_balloon(self):
        balloon_x = random.randint(0, self.screen_width - self.balloon_radius * 2)
        balloon_y = 0
        if len(self.special_balloons) % 30 == 0:
            self.special_balloons.append([balloon_x, balloon_y, "black"])
        elif len(self.special_balloons) % 20 == 0:
            self.special_balloons.append([balloon_x, balloon_y, "pink"])

    def show_result_screen(self):
        self.screen.fill((146, 125, 213))  # Ekranı siyah renge ayarla

        font = pygame.font.Font(None, 36)

        score_text = font.render(f"Toplam Balon: {self.popped_balloons}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 40))

        points_text = font.render(f"Toplam Puan: {self.score}", True, (255, 255, 255))
        points_rect = points_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))

        black_balloons_text = font.render(f"Siyah Balonlar: {self.black_balloons_popped}", True, (255, 255, 255))
        black_balloons_rect = black_balloons_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 40))

      

        self.screen.blit(score_text, score_rect)
        self.screen.blit(points_text, points_rect)
        self.screen.blit(black_balloons_text, black_balloons_rect)
       

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Enter tuşuna basıldığında
                        waiting = False  # Ekranı kapat
                        self.reset_game()  # Oyunu sıfırla ve tekrar başlat

    def reset_game(self):
        self.popped_balloons = 0
        self.black_balloons_popped = 0
        self.pink_balloons_popped = 0
        self.score = 0
        self.balloon_speed = 3
        self.speed_increase_threshold = 5
        self.balloons = []
        self.special_balloons = []
        self.sure = self.game_duration
        self.clock.tick(60)

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        self.show_result_screen()

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
                        self.black_balloons_popped += 1
                    elif special_balloon[2] == "pink":
                        self.score += 10
                        self.pink_balloons_popped += 1

            self.screen.fill(self.color)

            for balloon in self.balloons:
                pygame.draw.circle(self.screen, self.balloon_color, (balloon[0], balloon[1]), self.balloon_radius)

            for special_balloon in self.special_balloons:
                if special_balloon[2] == "black":
                    pygame.draw.circle(self.screen, (0, 0, 0), (special_balloon[0], special_balloon[1]), self.balloon_radius)
                elif special_balloon[2] == "pink":
                    pygame.draw.circle(self.screen, (255, 182, 193), (special_balloon[0], special_balloon[1]), self.balloon_radius)

            pygame.draw.rect(self.screen, (255, 248, 220), (self.player_x, self.player_y, self.player_width, self.player_height))

            pygame.font.init()
            font = pygame.font.Font(None, 40)
            text = font.render(f"Puan: {self.score}", True, (248, 248, 255))
            self.screen.blit(text, (10, 10))

            sure_text = font.render(f"Süre: {int(self.sure)}", True, (248, 248, 255))
            self.screen.blit(sure_text, (self.screen_width - 120, 10))

            self.sure -= 1 / 60  # Zamanı azalt

            if self.sure <= 0:
                self.show_result_screen()

            pygame.display.flip()
            self.clock.tick(60)
            
            

        pygame.quit()
"""
if __name__ == "__main__":
    oyun = Oyun(800, 600, 30)  # Ekran genişliği, yüksekliği ve oyun süresi (saniye cinsinden)
    oyun.main_loop()
"""