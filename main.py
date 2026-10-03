#import
import pygame
import sys 
import random 
from src.settings import SCREEN_HEIGHT,SCREEN_WIDTH,FPS,TITLE,GRAVITY, WHITE, GRAY
from src.player import Player
from src.obstacle import Cactus


def main():
    # 1. Inisialisasi Pygame & Layar
    pygame.init()
    current_width = 600
    current_height = 600
    screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)
    clock = pygame.time.Clock()

    pygame.display.set_caption(TITLE)  

    # 2. Inisialisasi Objek
    player = Player()
    player_group = pygame.sprite.GroupSingle(player)
    obstacle_group = pygame.sprite.Group()

    # 3. Timer Spawn
    SPAWN_OBSTACLE = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_OBSTACLE, 1500)

    # DEKLARASI VARIABEL KONTROL GAME (HARUS DI SINI / SEBELUM WHILE)
   
    running = True
    game_over = False
    is_fullscreen = False  # <--- PASTIKAN BARIS INI ADA DI SINI

    # 4. Game Loop Utama
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Penanganan Toggle Fullscreen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    is_fullscreen = not is_fullscreen  # Sekarang aman dipanggil!
                    if is_fullscreen:
                        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

                if not game_over and event.key in (pygame.K_SPACE, pygame.K_UP):
                    player.jump()

            if event.type == SPAWN_OBSTACLE and not game_over:
                curr_w, curr_h = screen.get_size()
                Cactus(curr_w, curr_h, obstacle_group)

            if game_over and event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_r):
                game_over = False
                player.is_dead = False
                obstacle_group.empty()

        # Update Logic & Render
        curr_w, curr_h = screen.get_size()

        if not game_over:
            player_group.update()
            obstacle_group.update()

            if pygame.sprite.spritecollide(player, obstacle_group, False):
                game_over = True
                player.is_dead = True
                player.update()

        screen.fill(WHITE)

        ground_y = int(curr_h * 0.7)
        pygame.draw.line(screen, GRAY, (0, ground_y), (curr_w, ground_y), 2)

        player_group.draw(screen)
        obstacle_group.draw(screen)

        if game_over:
            font = pygame.font.SysFont("arial", 30, bold=True)
            teks = font.render("Game Over - Press Space to Restart", True, GRAY)
            screen.blit(teks, (curr_w // 2 - teks.get_width() // 2, curr_h // 2))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()





