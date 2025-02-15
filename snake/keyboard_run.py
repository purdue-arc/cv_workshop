import pygame
import sys
from snake_game import SnakeGame, SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE

FPS = 10  # Frames per second, controls how fast the snake moves

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game (Keyboard Control)")
    clock = pygame.time.Clock()

    game = SnakeGame()

    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Up arrow or W
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    game.change_direction((0, -TILE_SIZE))
                # Down arrow or S
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    game.change_direction((0, TILE_SIZE))
                # Left arrow or A
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.change_direction((-TILE_SIZE, 0))
                # Right arrow or D
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.change_direction((TILE_SIZE, 0))

        # Update the game logic
        game.update()

        # If game over, you could choose to stop the loop or display a message
        if game.game_over:
            running = False  # For simplicity, end the game

        # Draw everything
        game.draw(screen)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
