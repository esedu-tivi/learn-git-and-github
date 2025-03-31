import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self):
        self.width = 30
        self.height = 30
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(0, SCREEN_HEIGHT - self.height)
        self.speed_x = 3
        self.speed_y = 3
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off the walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Red enemy