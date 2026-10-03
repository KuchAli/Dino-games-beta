import os 

# konfigurasi layar
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# Konfigurasi Fullscreen
FULLSCREEN_WIDTH = 1920
FULLSCREEN_HEIGHT = 1080

FPS= 60
TITLE= "DinoRun"

# fisika game 
GRAVITY = 0.6            # Kekuatan gravitasi yang menarik Dino ke bawah
JUMP_FORCE = -12         # Kecepatan awal saat Dino melompat (minus = ke atas)
GAME_SPEED = 7           # Kecepatan scrolling tanah & rintangan
# warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (83, 83, 83)

# posisi karakter
DINO_START_X = 20        # Posisi Dino dari kiri layar
DINO_START_Y = 415       # Posisi pijakan kaki Dino dari atas layar

#assets
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
IMG_DIR = os.path.join(ASSETS_DIR, "images")
SOUND_DIR = os.path.join(ASSETS_DIR, "sounds")