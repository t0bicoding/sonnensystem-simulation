import pygame # pyright: ignore[reportMissingImports]

class World:       
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 0), (200,200), 30)