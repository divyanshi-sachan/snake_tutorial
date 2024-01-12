import pygame
import random

class Snake:
    def __init__(self):
        self.length_of_snake = 1
        self.positions = [pygame.math.Vector2(10, 10)]
        self.direction = pygame.math.Vector2(0, 10)
        self.change_to = self.direction
        self.food_position = self.generate_food()
        self.score = 0

    def draw(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(pos.x, pos.y, 10, 10))

        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.food_position.x, self.food_position.y, 10, 10))

    def move(self):
        self.positions.insert(0, self.positions[0] + self.direction)

        if (
            self.positions[0].x < 0
            or self.positions[0].x >= 640
            or self.positions[0].y < 0
            or self.positions[0].y >= 480
        ):
            self.reset_snake()
        elif self.positions[0] == self.food_position:
            self.score += 1
            self.food_position = self.generate_food()
        elif self.positions[0] in self.positions[1:]:
            self.reset_snake()
        if len(self.positions) > self.length_of_snake:
            self.positions.pop()

    def change_direction(self, direction):
        self.change_to = direction

    def generate_food(self):
        food_x = round(random.randrange(0, 640 - 10) / 10.0) * 10.0
        food_y = round(random.randrange(0, 480 - 10) / 10.0) * 10.0
        return pygame.math.Vector2(food_x, food_y)

    def reset_snake(self):
        self.positions = [pygame.math.Vector2(10, 10)]
        self.length_of_snake = 1
        self.food_position = self.generate_food()
        self.score = 0

    def update(self):
        self.direction = self.change_to
        self.move()