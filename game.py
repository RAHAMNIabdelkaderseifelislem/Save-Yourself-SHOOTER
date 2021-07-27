from sounds import SoundManager
import pygame
from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent


class Game:
    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_monsters = pygame.sprite.Group()
        self.isPlaying = False
        self.comet_event = CometFallEvent(self)
        self.soundManager = SoundManager()
        self.score = 0
        self.pressed = {}
        self.font = pygame.font.Font("assets/PottaOne-Regular.ttf", 25)

    def start(self):
        self.isPlaying = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.isPlaying = False
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.score = 0
        self.soundManager.play('gameOver')

    def update(self, screen):
        scoreText = self.font.render(f"Score: {self.score}", 1, (0, 0, 0))
        screen.blit(scoreText, (20, 20))
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.comet_event.update_bar(screen)
        self.player.update_animation()
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectiles.draw(screen)
        
        
        self.all_monsters.draw(screen)

        self.comet_event.all_comets.draw(screen)
        
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monsterClassName):
        self.all_monsters.add(monsterClassName.__call__(self))