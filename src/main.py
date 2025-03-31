import pygame
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Pygame Example")
    
    clock = pygame.time.Clock()
    game = Game(screen, clock)
    game.start_game()

    pygame.quit()

if __name__ == "__main__":
    main()