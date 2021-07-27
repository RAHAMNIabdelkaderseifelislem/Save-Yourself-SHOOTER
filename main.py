import pygame
import math
from game import Game
pygame.init()

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("Save Yourself SHOOTER")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')
 
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil( screen.get_width() / 4)

play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil( screen.get_width() / 3.33)
play_button_rect.y = math.ceil( screen.get_height() / 2)

game = Game()

running = True

while running:
    screen.blit(background, (0, -200))

    if game.isPlaying:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Closed")
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                if game.isPlaying:
                    game.player.launch_projectile()
                else:
                    game.start()
                    game.soundManager.play('click')
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                game.soundManager.play('click')
    
    clock.tick(FPS)