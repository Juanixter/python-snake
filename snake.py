from pygame import Vector2
import pygame
from constants import DARK_GREEN, cell_size, OFFSET

class Snake:

    def __init__(self, screen : pygame.Surface):

        self.screen = screen
        self.body = [ Vector2(6,9), Vector2(5,9), Vector2(4,9) ]
        self.direction = Vector2(1,0)
        self.add_segment = False
        self.eat_sound = pygame.mixer.Sound("sounds/eat.mp3")
        self.wall_hit_sound = pygame.mixer.Sound("sounds/wall.mp3")

    def draw(self):
        for segment in self.body:
            segment_rect = pygame.Rect( OFFSET + segment.x * cell_size, OFFSET + segment.y * cell_size, cell_size, cell_size )
            pygame.draw.rect(
                surface = self.screen,
                color = DARK_GREEN,
                rect = segment_rect,
                border_radius = 7
            )

    def update(self):
        self.body.insert(0, self.body[0] + self.direction)
        if self.add_segment:
            self.add_segment = False
        else:
            self.body.pop()

    def reset(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
        self.direction = Vector2(1,0)