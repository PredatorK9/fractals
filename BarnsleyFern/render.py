import pygame
import random
from utils import calculate, original

WINDOW = (500, 600)
GRAY = (30, 30, 30)
GREEN = (00, 128, 00)

display = pygame.display.set_mode(WINDOW)
pygame.display.set_caption('Barnsley Fern')
clock = pygame.time.Clock()


def draw(x, y):
    for _ in range(10):
        x, y = calculate(x, y, random.random(), original)
        X, Y = x*99, y*59
        pygame.draw.circle(display, GREEN,
            [int(WINDOW[0]//2 - 20 + X) , int(WINDOW[1] - Y)], 1)
    pygame.display.update()
    return x, y


def main():
    absicca, ordinate = 0.0, 0.0
    display.fill(GRAY)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        absicca, ordinate = draw(absicca, ordinate)
        clock.tick(60)

if __name__ == '__main__':
    main()