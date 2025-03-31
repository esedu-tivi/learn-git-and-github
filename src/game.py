import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, FPS
from enemy import Enemy

class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 50, 50)
        self.enemy = Enemy()
        self.game_over = False

    def start_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.game_over:
                self.update()
                self.check_collision()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FPS)

    def update(self):
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= 5
        if keys[pygame.K_RIGHT]:
            self.player.x += 5
        if keys[pygame.K_UP]:
            self.player.y -= 5
        if keys[pygame.K_DOWN]:
            self.player.y += 5
            
        # Keep player in bounds
        # self.player.clamp_ip(self.screen.get_rect())
        
        # Update enemy
        self.enemy.update()

    def check_collision(self):
        if self.player.colliderect(self.enemy.rect):
            self.game_over = True

    def draw(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, (0, 0, 255), self.player)  # Blue player
        self.enemy.draw(self.screen)
        
        if self.game_over:
            font = pygame.font.Font(None, 74)
            text = font.render('Game Over', True, (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            self.screen.blit(text, text_rect)