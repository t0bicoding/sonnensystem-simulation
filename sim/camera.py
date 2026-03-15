import pygame # pyright: ignore[reportMissingImports]

class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.zoom = 1.0
        self.zoom_factor = 1.1
        self.min_zoom = 0.001
        self.max_zoom = 10.0
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.dragging = False
        self.last_mouse_pos = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                self.zoom *= self.zoom_factor
            elif event.y < 0:
                self.zoom /= self.zoom_factor
            self.zoom = max(self.min_zoom, min(self.max_zoom, self.zoom))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            self.dragging = True
            self.last_mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            self.dragging = False
            self.last_mouse_pos = None
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            dx = event.pos[0] - self.last_mouse_pos[0]
            dy = event.pos[1] - self.last_mouse_pos[1]
            self.offset_x += dx
            self.offset_y += dy
            self.last_mouse_pos = event.pos

    def apply(self, x, y):
        cx = self.screen_width / 2
        cy = self.screen_height / 2
        screen_x = cx + (x - cx) * self.zoom + self.offset_x
        screen_y = cy + (y - cy) * self.zoom + self.offset_y
        return screen_x, screen_y

    def apply_radius(self, radius):
        return radius * self.zoom
