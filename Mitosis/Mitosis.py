import pygame
import random
from cell import Cell

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
        
        #Cell setup
        self.cells = pygame.sprite.Group()
        self.initial_cell_count = 5
        self.cell_setup(self.initial_cell_count)
        
        
        
        
        
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
                
    def cell_setup(self, cell_count):
        for i in range(cell_count):
            form = random.choice(("circle", "ellipse"))
            x = random.randint(100, 700)
            y = random.randint(100, 700)
            cell_sprite = Cell(self.background, form, x, y)
            self.cells.add(cell_sprite)
    
    # Run Animation
    def run_animation(self):
        self.cells.update(1)
        self.app.screen.blit(self.background, (0, 0))
        self.cells.draw(self.app.screen)


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
