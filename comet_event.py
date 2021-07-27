import pygame
from comet import Comet


class CometFallEvent :
    
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 1000
        self.game = game
        self.all_comets = pygame.sprite.Group()

    
    def add_percent(self):
        self.percent += self.percent_speed / 100
    
    def is_full_loaded(self):
        return self.percent >= 100
    
    def meteor_fall(self):
        self.all_comets.add(Comet(self))
    
    def reset_percent(self):
        self.percent = 0

    def attempt_fall(self):
        if self.is_full_loaded():
            self.meteor_fall()        
            self.reset_percent()
        pass

    def update_bar(self,surface):
        
        pygame.draw.rect(surface, (0,0,0),[
            0,surface.get_height() - 20 ,surface.get_width(),10
        ])
        
        self.add_percent()

        self.attempt_fall()
        pygame.draw.rect(surface, (187,11,11),[
            0,surface.get_height() - 20,(surface.get_width() / 100) * self.percent,10
        ])
