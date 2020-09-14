import pygame
from utils import turtle, generate, length, axiom_init
import time

BG = (0, 0, 0)
STROKE = (255, 255, 255)

offsetX ,offsetY = -50, -275
HEIGHT, WIDTH = 600, 600

display = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('L System')
clock = pygame.time.Clock()

def draw(start_pos, end_pos):
    pygame.draw.line(display, STROKE, (WIDTH//2 + offsetX + start_pos[0],
            HEIGHT//2 - offsetY - start_pos[1]), 
            (WIDTH//2 + offsetX + end_pos[0], HEIGHT//2 - offsetY - end_pos[1]))
    pygame.display.update()
    return end_pos

def main():
    axiom = axiom_init()
    x, y = 0, length

    while True:
        display.fill(BG)
        angle = 0
        position = (0, 0)
        for character in axiom:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            position, angle, x, y = turtle(draw, character,
                position[0], position[1], angle, x, y)

        axiom = generate(axiom)
        clock.tick(1)
        

if __name__ == "__main__":
    main()