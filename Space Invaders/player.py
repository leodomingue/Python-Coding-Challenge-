import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, WIDTH):
        super().__init__()
        self.image = pygame.image.load("Space Invaders/assets/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = position)
        self.speed = 5
        self.width = WIDTH
        self.ready = True
        self.shoot_time = 0
        self.shoot_cc = 1000
        
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] and self.rect.right < self.width:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]and self.rect.x > 0:
            self.rect.x -= self.speed
            
        if keys[pygame.K_SPACE] and self.ready is True:
            self.shoot()
            self.ready = False
            self.shoot_time = pygame.time.get_ticks()
            
    def recharge_shoot(self):
        if self.ready is False:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.shoot_cc:
                self.ready= True
        
    
    
    def update(self):
        self.get_input()
        self.recharge_shoot()
        
    def shoot(self):
        print("Miau")