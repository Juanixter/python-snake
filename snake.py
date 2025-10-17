import pygame
import sys

pygame.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

screen = pygame.display.set_mode((750,750))

pygame.display.set_caption("Python Snake")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(GREEN)
    pygame.display.update()
    clock.tick(60)