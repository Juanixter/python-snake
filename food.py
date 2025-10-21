import random
from typing import List
from constants import cell_size, number_of_cells, OFFSET, DARK_GREEN
import pygame
from pygame import Vector2

class Food:

    def __init__(self, screen: pygame.Surface, snake_body: List[Vector2]):

        self.screen = screen
        self.position = self.generate_random_pos(snake_body)
        self.food_surface = pygame.image.load('graphics/food.png')

    def draw(self):

        food_rect = pygame.Rect( OFFSET + self.position.x * cell_size, OFFSET + self.position.y * cell_size, cell_size, cell_size)

        if cell_size >= 28:
            self.screen.blit(
                source = self.food_surface,
                dest = food_rect,
                )
        else:
            pygame.draw.rect(
                surface = self.screen,
                color = DARK_GREEN,
                rect = food_rect
            )
        
    def generate_random_cell(self) -> Vector2:
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        return Vector2(x, y)

    def generate_random_pos(self, snake_body: List[Vector2]) -> Vector2:
        
        position = self.generate_random_cell()
        while position in snake_body:
            position = self.generate_random_cell()

        return position