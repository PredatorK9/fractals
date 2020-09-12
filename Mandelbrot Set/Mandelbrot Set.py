import random
import pygame
import math

WINDOW = (600, 600)
BLACK = (0, 0, 0)

display = pygame.display.set_mode(WINDOW)
pygame.display.set_caption('Mandelbrot Set')
clock = pygame.time.Clock()


def sqrComplex(complex : (float, float)) -> (float, float):
    '''
    A small function to calculate the square of
    a complex number
    '''
    real = complex[0]**2 - complex[1]**2
    imaginary = 2*complex[0]*complex[1]

    return real, imaginary


def draw(complex, shade, scale):

    scaledY = complex[1]*scale
    scaledX = complex[0]*scale

    pygame.draw.circle(display,
        shade, [int(WINDOW[1]//2 + scaledX), int(WINDOW[0]//2 - scaledY)], 0)
    pygame.display.update()


def main():

    minX = -1.75
    maxX = 1.75

    minY = -1.75
    maxY = 1.75

    maxiterations = 255
    scale = 170

    display.fill(BLACK)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        real = random.uniform(minX, maxX)
        imaginary = random.uniform(minY, maxY)

        c_real = real
        c_imaginary = imaginary

        for i in range(1, maxiterations+1):
            real, imaginary = sqrComplex((real, imaginary))
            real = real + c_real
            imaginary = imaginary + c_imaginary

            color = i / maxiterations
            color = math.sqrt(color) * 255

            if i == maxiterations:
                color = 0

            if abs(real + imaginary) > 4.0:
                break

        SHADE = (color, color, color)
        draw((c_real, c_imaginary), SHADE, scale)
        clock.tick(60)


if __name__ == "__main__":
    main()