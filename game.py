import pygame
import sys

from food import Food
from constants import cell_size, number_of_cells, GREEN
from snake import Snake

pygame.init()
pygame.display.set_caption("Python Snake")

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))

clock = pygame.time.Clock()

food_surface = pygame.image.load('graphics/food.png')

food = Food( screen = screen, food_surface = food_surface )
snake = Snake( screen = screen )

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(
    event = SNAKE_UPDATE,
    millis = 200
)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snake.update()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != pygame.Vector2(0,1):
                snake.direction = pygame.Vector2(0,-1)
            if event.key == pygame.K_DOWN and snake.direction != pygame.Vector2(0,-1):
                snake.direction = pygame.Vector2(0,1)
            if event.key == pygame.K_LEFT and snake.direction != pygame.Vector2(1,0):
                snake.direction = pygame.Vector2(-1,0)
            if event.key == pygame.K_RIGHT and snake.direction != pygame.Vector2(-1,0):
                snake.direction = pygame.Vector2(1,0)
    
    # DRAWING
    screen.fill(GREEN)
    food.draw()
    snake.draw()

    pygame.display.update()
    clock.tick(60)