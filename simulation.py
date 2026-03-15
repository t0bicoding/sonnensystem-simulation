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
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                   
            screen.fill("black")
            world.draw()
            
            pygame.display.flip()

            clock.tick(self.FPS)

        pygame.quit()
