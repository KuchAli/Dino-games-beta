import os 
import pygame 
from src.settings import IMG_DIR, DINO_START_X, DINO_START_Y, GRAVITY, JUMP_FORCE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Helper function untuk memuat gambar transparan (PNG tanpa background)
        def load_sprite(filename):
            path = os.path.join(IMG_DIR, filename)
            return pygame.image.load(path).convert_alpha()

        # 1. Load sprite khusus karakter Dino
        self.run_frame1 = load_sprite("Dino-run.png")
        self.run_frame2 = load_sprite("Dino-run-1.png")
        self.jump_frame = load_sprite("Dino.png")
        self.dead_frame = load_sprite("Dino-game-over.png")

        # 2. Masukkan frame lari ke dalam list animasi
        self.run_frames = [self.run_frame1, self.run_frame2]
        self.frame_index = 0
        self.anim_speed = 0.15  # Kecepatan ganti animasi kaki

        # Gambar awal dan hitbox
        self.image = self.run_frames[0]
        self.rect = self.image.get_rect(bottomleft=(DINO_START_X, DINO_START_Y))

        # Status fisika
        self.vel_y = 0
        self.is_jumping = False
        self.is_dead = False

    def jump(self):
        # Mekanik lompat
        if not self.is_jumping and not self.is_dead:
            self.vel_y = JUMP_FORCE
            self.is_jumping = True

    def animate(self):
        # Simpan posisi bagian bawah kaki sebelum mengganti gambar
        bottom_left = self.rect.bottomleft

        # Memutar animasi berdasarkan keadaan dino
        if self.is_dead:
            self.image = self.dead_frame
        elif self.is_jumping:
            self.image = self.jump_frame
        else:
            # Berganti animasi lari (Dino-run.png <-> Dino-run-1.png)
            self.frame_index += self.anim_speed 
            if self.frame_index >= len(self.run_frames):
                self.frame_index = 0
            self.image = self.run_frames[int(self.frame_index)]

        # Sesuaikan kembali rect agar posisi lantai (bottom) tidak bergeser saat ukuran sprite beda
        self.rect = self.image.get_rect(bottomleft=bottom_left)

    def apply_gravity(self):
        # Hitungan gravitasi 
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Batas lantai
        if self.rect.bottom >= DINO_START_Y:
            self.rect.bottom = DINO_START_Y
            self.vel_y = 0
            self.is_jumping = False

    def update(self):
        self.apply_gravity()
        self.animate()

    def draw(self, surface):
        surface.blit(self.image, self.rect)