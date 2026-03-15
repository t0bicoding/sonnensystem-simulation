import pygame # pyright: ignore[reportMissingImports]
from sim.world import World
from sim.camera import Camera

class Simulation:
    WindowWidth = 1920
    WindowHeight = 1080
    FPS = 60

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
        clock = pygame.time.Clock()
        camera = Camera(self.WindowWidth, self.WindowHeight)
        world = World(screen, self.WindowWidth / 2, self.WindowHeight / 2)

        background = pygame.image.load("assets/Pictures/milky_way.jpg")
        background = pygame.transform.scale(background, (self.WindowWidth, self.WindowHeight))
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                camera.handle_event(event)

            screen.blit(background, (0,0))
            #screen.fill("#0C0C0C")

            dt = clock.tick(self.FPS) / 1000
            world.update(dt)
            world.draw(camera)

            pygame.display.flip()

        pygame.quit()
