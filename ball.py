import pygame
from math import floor

class Ball(pygame.sprite.Sprite):
    GRAVITY = 0.98

    def __init__(self, screen, x, y, size, color=(0, 0, 255)) -> None:
        super(Ball, self)
        self.SCREEN: pygame.display = screen
        self.pos = pygame.Vector2(x, y)
        self.size = size
        self.color = color
        self.vx = 25
        self.vy = 25
        self.ax = 0
        self.ay = -self.GRAVITY

    def update(self, dt) -> None:
        self.pos.x = 250
        self.pos.y -= self.vy
        self.vy += self.ay
        if self.pos.y + self.size >= self.SCREEN.get_height():
            self.vy = -self.vy*0.75


    def draw(self) -> None:
        pygame.draw.circle(self.SCREEN, self.color, self.pos, self.size)

    
    