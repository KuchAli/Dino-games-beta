import pygame

class SpriteSheet:
    def __init__(self, filename):
        # Gunakan .convert() tanpa alpha agar colorkey bisa bekerja 100% sempurna
        self.sheet = pygame.image.load(filename).convert()

    def getImage(self, x, y, width, height, colorkey=None):
        # Buat surface standar (tanpa SRCALPHA agar colorkey berfungsi optimal)
        image = pygame.Surface((width, height))

        # Ambil potongan dari spritesheet
        image.blit(self.sheet, (0, 0), (x, y, width, height))

        # Hapus warna background jika colorkey diberikan
        if colorkey is not None:
            image.set_colorkey(colorkey)

        return image