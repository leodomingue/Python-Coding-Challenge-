import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, pos,speed , HEIGHT):
        super().__init__()
        self.image = pygame.Surface((4,20))
        self.image.fill("WHITE")
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        
        self.height = HEIGHT
        
    def update(self):
        self.rect.y -= self.speed
        self.destroy()
        
    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height:
            self.kill()