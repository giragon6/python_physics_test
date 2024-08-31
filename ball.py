import pygame
from math import floor

class Ball(pygame.sprite.Sprite):
    GRAVITY = 0.98

    def __init__(self, screen, x, y, size, vx=0, color=(0, 0, 255)) -> None:
        super(Ball, self)
        self.SCREEN: pygame.display = screen
        self.pos = pygame.Vector2(x, y)
        self.size = size
        self.color = color
        self.vx = vx
        self.vy = 0
        self.ax = 0
        self.ay = -self.GRAVITY

    def update(self) -> None:
        if (self.pos.y + self.size >= self.SCREEN.get_height()) or (self.pos.y - self.size <= 0):
            self.vy = floor(-self.vy*0.75)
        self.pos.y -= self.vy
        self.vy += self.ay 

        if (self.pos.x >= self.SCREEN.get_width()) or (self.pos.x <= 0):
            self.vx = floor(-self.vx*0.75)
        self.pos.x += self.vx
        self.vx += self.ax  
                 

    def draw(self) -> None:
        pygame.draw.circle(self.SCREEN, self.color, self.pos, self.size)

    
    