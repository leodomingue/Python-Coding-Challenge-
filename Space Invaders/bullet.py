from typing import Any
import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, pos, HEIGHT):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill("WHITE")
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5
        
        self.height = HEIGHT
        
    def update(self):
        self.rect.y -= 5
        self.destroy()
        
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height:
            self.kill()