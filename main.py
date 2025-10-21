import pygame
import sys
import constants
from game import Game

pygame.init()

title_font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 40)

pygame.display.set_caption(constants.GAME_NAME)

screen = pygame.display.set_mode(( 2 * constants.OFFSET + constants.cell_size * constants.number_of_cells, 2 * constants.OFFSET + constants.cell_size * constants.number_of_cells))

clock = pygame.time.Clock()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(
    event = SNAKE_UPDATE,
    millis = 200
)

game = Game( screen = screen )

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if game.state == "STOPPED":
                game.state = "RUNNING"

            if event.key == pygame.K_UP and game.snake.direction != pygame.Vector2(0,1):
                game.snake.direction = pygame.Vector2(0,-1)
            if event.key == pygame.K_DOWN and game.snake.direction != pygame.Vector2(0,-1):
                game.snake.direction = pygame.Vector2(0,1)
            if event.key == pygame.K_LEFT and game.snake.direction != pygame.Vector2(1,0):
                game.snake.direction = pygame.Vector2(-1,0)
            if event.key == pygame.K_RIGHT and game.snake.direction != pygame.Vector2(-1,0):
                game.snake.direction = pygame.Vector2(1,0)
    
    # DRAWING
    screen.fill(constants.GREEN)
    pygame.draw.rect(
        screen, 
        constants.DARK_GREEN, 
        (constants.OFFSET-5, constants.OFFSET-5, constants.cell_size*constants.number_of_cells+10, constants.cell_size*constants.number_of_cells+10), 
        5
    )
    game.draw()

    title_surface = title_font.render(constants.GAME_NAME, True, constants.DARK_GREEN)
    score_surface = score_font.render(str(game.score), True, constants.DARK_GREEN)
    screen.blit(title_surface, (constants.OFFSET-5, 20))
    screen.blit(score_surface, (constants.OFFSET-5, constants.OFFSET + constants.cell_size * constants.number_of_cells + 10))

    pygame.display.update()
    clock.tick(60)