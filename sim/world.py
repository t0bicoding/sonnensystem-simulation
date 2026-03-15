from body.star import Star
from body.planet import Planet
import json

class World:
    def __init__(self, screen, center_x, center_y):
        self.screen = screen
        with open("data/stars.json") as f:
            stars_data = json.load(f)
            
        sun = stars_data["sun"]
        self.star = Star(sun["color"], center_x, center_y, sun["radius"])
        
        self.mercury = Planet(center_x, center_y, "mercury")
        self.venus = Planet(center_x, center_y, "venus")
        self.earth = Planet(center_x, center_y, "earth")
        self.mars = Planet(center_x, center_y, "mars")
        self.jupiter = Planet(center_x, center_y, "jupiter")
        self.saturn = Planet(center_x, center_y, "saturn")
        self.uranus = Planet(center_x, center_y, "uranus")
        self.neptun = Planet(center_x, center_y, "neptun")
        
    def draw(self):
        self.star.draw(self.screen)
        self.mercury.draw(self.screen)
        self.venus.draw(self.screen)
        self.earth.draw(self.screen)
        self.mars.draw(self.screen)
        self.jupiter.draw(self.screen)
        self.saturn.draw(self.screen)
        self.uranus.draw(self.screen)
        self.neptun.draw(self.screen)
    
    def update(self, dt):
        self.earth.update(dt)
        self.mercury.update(dt)
        self.venus.update(dt)
        self.mars.update(dt)
        self.jupiter.update(dt)
        self.saturn.update(dt)
        self.uranus.update(dt)
        self.neptun.update(dt)
        