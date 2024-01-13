import pygame

# Singleton tasarım deseni kullanılmıştır.

class SoundManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SoundManager, cls).__new__(cls)
            pygame.mixer.init()
            cls._instance.normal_balloon_sound = pygame.mixer.Sound("ses/yt5s.io - Balloon Pop Sound effect (320 kbps).mp3")
            cls._instance.black_balloon_sound = pygame.mixer.Sound("ses/yt5s.io - Breaking glass sound effect (320 kbps).mp3")
            cls._instance.pink_balloon_sound = pygame.mixer.Sound("ses/Mario Coin - Free Sound Effect.mp3")
            cls._instance.ice_sound = pygame.mixer.Sound("ses/Ice Cracking - Sound Effect HD.mp3")
        return cls._instance

    def play_normal_balloon_sound(self):
        self.normal_balloon_sound.play()

    def play_black_balloon_sound(self):
        self.black_balloon_sound.play()

    def play_pink_balloon_sound(self):
        self.pink_balloon_sound.play()

    def play_ice_sound(self):
        self.ice_sound.play()
