import os
import random
import pygame
from src.settings import IMG_DIR, GAME_SPEED


class Cactus(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, *groups):
        # Panggil init parent class Sprite dengan kelompok group jika ada
        super().__init__(*groups)

        def load_cactus(filename):
            path = os.path.join(IMG_DIR, filename)
            return pygame.image.load(path).convert_alpha()

        cacti_image = [
            load_cactus("Cactus.png"),
            load_cactus("Cactus-1.png"),
            load_cactus("Cactus-2.png"),
            load_cactus("Cactus-big.png")
        ]
        selected_file = random.choice(cacti_image)

        self.image = random.choice(cacti_image)
        
        # Hitung posisi tanah sesuai tinggi layar aktif (70% dari tinggi layar)
        ground_y = int(screen_height * 0.7)
        
        # Buat rect dengan posisi awal di luar kanan layar
        self.rect = self.image.get_rect(bottomleft=(screen_width + 50, ground_y))

        # Inisialisasi awal hitbox
        if selected_file == "Cactus-big.png":
            # Potong lebih banyak untuk kaktus besar (misal: -35px lebar, -25px tinggi)
            self.hitbox = self.rect.inflate(-45, -30)
        else:
            # Potong standar untuk kaktus biasa
            self.hitbox = self.rect.inflate(-30, -21)

    def update(self):
        # 1. Gerakkan rect gambar kaktus ke kiri
        self.rect.x -= GAME_SPEED

        # 2. PENTING: Pindahkan posisi pusat hitbox agar SELALU MENGIKUTI rect kaktus
        self.hitbox.center = self.rect.center

        # Hapus objek jika sudah lewat layar sebelah kiri
        if self.rect.right < 0:
            self.kill()