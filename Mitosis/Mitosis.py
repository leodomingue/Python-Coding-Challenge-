import pygame
import random

#Variables
FPS = 60
WIDTH = 800
HEIGHT = 800

# RGB color values
RED = (200, 210)
GREEN = (170, 180)
BLUE = (100, 115)


#Class Logic
class Animation:
    def __init__(self, app):
        self.app = app
        self.background = self.recreate_backgroud()
        
    # Generate a random color within the specified range
    def random_color(self, color_range):
        return (random.randint(color_range[0], color_range[1]))
        
        
    # Recreate the background with randomly colored rectangles
    def recreate_backgroud(self):
        background = pygame.Surface((WIDTH, HEIGHT))
        for y in range(0, HEIGHT, 5):
            for x in range (0, WIDTH, 5):
                color = self.random_color(RED), self.random_color(GREEN), self.random_color(BLUE)
                pygame.draw.rect(background, color, (x, y, 5, 5))
        return background
                
    
    # Run Animation
    def run_animation(self):
        self.app.screen.blit(self.background, (0, 0))


#Class to Initialize app
class App:
    def __init__(self):
        # Initialize the screen and clock
        self.screen =  pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.animation = Animation(self)
        
        
    def run(self):
        while True:
            # Cap the frame rate
            self.clock.tick(FPS)
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
                    
            self.screen.fill("BLACK")
            self.animation.run_animation()
            
            
            # Update the display
            pygame.display.update()
            
        

if __name__ == "__main__":
    # Initialize pygame
    pygame.init()
    
    # Create an instance of the App class and run the game loop
    app = App()
    app.run()
