import pygame
import sys

pygame.init()

w,h = 800,600
screen = pygame.display.set_mode((w,h))

white = (255,255,255)
black = (0,0,0)


def midpoint_ellipse(xc, yc, rx, ry):
    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    # Region 1
    while 2*ry2*x < 2*rx2*y:
        screen.set_at((xc + x, yc + y), white)
        screen.set_at((xc - x, yc + y), white)
        screen.set_at((xc + x, yc - y), white)
        screen.set_at((xc - x, yc - y), white)

        if p1 < 0:
            x = x + 1
            y = y
            p1 = p1 + 2*ry2*x + ry2
        else:
            x = x + 1
            y = y - 1
            p1 = p1 + 2*ry2*x - 2*rx2*y + ry2

    # Region 2
    p2 = (ry2 * (x + 0.5) * (x + 0.5)) + (rx2 * (y - 1) * (y - 1)) - (rx2 * ry2)

    while y >= 0:
        screen.set_at((xc + x, yc + y), white)
        screen.set_at((xc - x, yc + y), white)
        screen.set_at((xc + x, yc - y), white)
        screen.set_at((xc - x, yc - y), white)

        if p2 > 0:
            y = y - 1
            x = x
            p2 = p2 + rx2 - 2*rx2*y
        else:
            x = x + 1
            y = y - 1
            p2 = p2 + 2*ry2*x - 2*rx2*y + rx2



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    midpoint_ellipse(300,300,50,100)
    pygame.display.flip()


