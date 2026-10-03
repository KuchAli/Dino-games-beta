import os 
import pygame 
from src.settings import IMG_DIR, DINO_START_X, GRAVITY, JUMP_FORCE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Helper function untuk memuat gambar transparan (PNG)
        def load_sprite(filename):
            path = os.path.join(IMG_DIR, filename)
            return pygame.image.load(path).convert_alpha()

        # 1. Load sprite khusus karakter Dino
        self.run_frame1 = load_sprite("Dino-run.png")
        self.run_frame2 = load_sprite("Dino-run-1.png")
        self.jump_frame = load_sprite("Dino.png")
        self.dead_frame = load_sprite("Dino-game-over.png")

        # 2. Frame animasi
        self.run_frames = [self.run_frame1, self.run_frame2]
        self.frame_index = 0
        self.anim_speed = 0.15

        # Gambar awal dan rect
        self.image = self.run_frames[0]
        
        # Posisi awal (Default tinggi 600, tanah di 70% -> 420)
        default_ground_y = int(600 * 0.7)
        self.rect = self.image.get_rect(bottomleft=(DINO_START_X, default_ground_y))
        
        # Hitbox (dikurangi sedikit dari rect agar tabrakan pas)
        self.hitbox = self.rect.inflate(-10, -10)

        # Status fisika
        self.vel_y = 0
        self.is_jumping = False
        self.is_dead = False

    def jump(self):
        if not self.is_jumping and not self.is_dead:
            self.vel_y = JUMP_FORCE
            self.is_jumping = True

    def animate(self):
        bottom_left = self.rect.bottomleft

        if self.is_dead:
            self.image = self.dead_frame
        elif self.is_jumping:
            self.image = self.jump_frame
        else:
            self.frame_index += self.anim_speed 
            if self.frame_index >= len(self.run_frames):
                self.frame_index = 0
            self.image = self.run_frames[int(self.frame_index)]

        self.rect = self.image.get_rect(bottomleft=bottom_left)

    # TAMBAHKAN parameter screen_height dengan default 600
    def apply_gravity(self, screen_height=600):
        # Tentukan posisi tanah dinamis (70% dari tinggi layar saat ini)
        ground_y = int(screen_height * 0.7)

        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Batas lantai dinamis
        if self.rect.bottom >= ground_y:
            self.rect.bottom = ground_y
            self.vel_y = 0
            self.is_jumping = False

    # UBAH di sini: Tambahkan screen_height=600 agar menerima argumen dari main.py
    def update(self, screen_height=600):
        self.apply_gravity(screen_height)
        self.animate()
        
        # Pastikan posisi hitbox selalu mengikuti rect utama
        self.hitbox.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)