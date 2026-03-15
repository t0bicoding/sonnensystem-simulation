import pygame # pyright: ignore[reportMissingImports]
from sim.world import World

class Simulation:
    WindowWidth = 1920
    WindowHeight = 1080
    FPS = 60

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        clock = pygame.time.Clock()
        world = World(screen, self.WindowWidth / 2, self.WindowHeight / 2)
        
        background = pygame.image.load("assets/Pictures/milkyway.jpg")
        background = pygame.transform.scale(background, (self.WindowWidth, self.WindowHeight))
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                   
            #screen.blit(background, (0,0))
            screen.fill("#0C0C0C")
            
            dt = clock.tick(self.FPS) / 1000
            world.update(dt)
            world.draw()
            
            pygame.display.flip()

            clock.tick(self.FPS)

        pygame.quit()
