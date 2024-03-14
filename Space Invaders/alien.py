import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, color,x, y):
        super().__init__()
        file_path = "Space Invaders/assets/" + color + ".png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft = (x, y))
        
        if color == "red":
            self.value= 100
        elif color == "green":
            self.value = 200
        elif color == "yellow":
            self.value = 300
        
    def update(self, direction):
        self.rect.x += direction
    
class Extra(pygame.sprite.Sprite):
    def __init__(self, side, width):
        super().__init__()
        self.image = pygame.image.load("Space Invaders/assets/extra.png")
        
        if side == "right":
            x = width + 50
            self.speed = -3
        else:
            x = -50
            self.speed = 3
            
        self.rect = self.image.get_rect(topleft=(x,80))
        
        self.value = 1000
        
    def update(self):
        self.rect.x += self.speed