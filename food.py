import random
from constants import cell_size, number_of_cells
import pygame
from pygame import Surface, Vector2


class Food:

    def __init__(self, screen: pygame.Surface, food_surface: Surface):

        self.position = self.generate_random_pos()
        self.screen = screen
        self.food_surface = food_surface

    def draw(self):

        food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)

        self.screen.blit(
            source = self.food_surface,
            dest = food_rect
            )
        
    def generate_random_pos(self) -> Vector2:
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)

        position = Vector2(x, y)

        return position