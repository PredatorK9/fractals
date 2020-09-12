import pygame
import random
from utils import calculate, fern_type

fern = 'original' # type of fern i.e original or mutant

WINDOW = (500, 600)
GRAY = (30, 30, 30)
GREEN = (00, 128, 00)

display = pygame.display.set_mode(WINDOW)
pygame.display.set_caption('Barnsley Fern')
clock = pygame.time.Clock()


def draw(x, y):
    for _ in range(10):
        c=0.0
        scaleX = 99
        scaleY = 59

        x, y = calculate(x, y, random.random(), fern_type[fern])

        if fern == 'mutant':
            c = -80
            scaleX = 130
            scaleY = 70

        X, Y = x*scaleX, y*scaleY
        pygame.draw.circle(display, GREEN,
            [int(WINDOW[0]//2 - 20 + X) , int(WINDOW[1] - Y + c)], 0)
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