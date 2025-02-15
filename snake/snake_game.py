import pygame
import random

# Constants for screen size and tile size
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
TILE_SIZE = 20

class SnakeGame:
    def __init__(self):
        """
        Initialize the game state: snake position, food, direction, score, etc.
        """
        self.snake_body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (TILE_SIZE, 0)  # Move right by default
        self.food_position = self.spawn_food()
        self.game_over = False
        self.score = 0

    def spawn_food(self):
        """
        Randomly position food on the grid.
        """
        # Ensure the food is aligned to the TILE_SIZE grid.
        max_x = (SCREEN_WIDTH // TILE_SIZE) - 1
        max_y = (SCREEN_HEIGHT // TILE_SIZE) - 1
        x = random.randint(0, max_x) * TILE_SIZE
        y = random.randint(0, max_y) * TILE_SIZE
        return (x, y)

    def update(self):
        """
        Update the snake's position, check for collisions, handle food consumption.
        """
        if self.game_over:
            return

        # Current head position
        head_x, head_y = self.snake_body[0]

        # New head position after direction
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # Check boundary collisions (if head goes out of screen)
        if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
            self.game_over = True
            return

        # Check self-collision
        if new_head in self.snake_body:
            self.game_over = True
            return

        # Insert new head
        self.snake_body.insert(0, new_head)

        # If food is eaten
        if new_head == self.food_position:
            self.score += 1
            self.food_position = self.spawn_food()
        else:
            # Pop the tail
            self.snake_body.pop()

    def change_direction(self, new_direction):
        """
        Change the snake's direction if it's not directly opposite of the current direction.
        For example, if the snake is moving right, it can't instantly move left.
        """
        current_x, current_y = self.direction
        new_x, new_y = new_direction

        # Don’t allow reversing direction (e.g., going directly left from right)
        if (current_x + new_x == 0) and (current_y + new_y == 0):
            return

        self.direction = (new_x, new_y)

    def draw(self, surface):
        """
        Draw the snake, food, and score onto the given surface.
        """
        surface.fill((0, 0, 0))  # Clear screen with black

        # Draw the snake
        for x, y in self.snake_body:
            pygame.draw.rect(
                surface,
                (0, 255, 0),
                pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            )

        # Draw the food
        fx, fy = self.food_position
        pygame.draw.rect(
            surface,
            (255, 0, 0),
            pygame.Rect(fx, fy, TILE_SIZE, TILE_SIZE)
        )

        # You can also show the score text here if you like.
        # For now, we’ll keep it simple.

