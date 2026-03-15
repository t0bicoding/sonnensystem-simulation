import pygame # pyright: ignore[reportMissingImports]
from sim.world import World

class Simulation:
    WindowWidth = 1280
    WindowHeight = 720
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("black")
            World().draw(screen)
            
            pygame.display.flip()
            
            clock.tick(60)
        
        pygame.quit()
        