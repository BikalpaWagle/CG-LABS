#2d transformations: translation, rotation, and scaling
import pygame
import sys
import math

def translate(x, y, tx, ty):
    return x + tx, y + ty

def rotate(x, y, angle):
    radians = math.radians(angle)
    x = x*math.cos(radians) - y*math.sin(radians)
    y = x*math.sin(radians) + y*math.cos(radians)
    return x, y

def scale(x, y, sx, sy):
    return x * sx, y * sy

pygame.init()
WIDTH = 1000
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformations: Translation, Rotation, Scaling Apil Maraseni 012")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    x1, y1 = 100, 100
    x2, y2 = 700, 200
    screen.fill(BLACK)
    # Original line
    pygame.draw.line(screen, WHITE, (x1, y1), (x2, y2), 2)

    tx1, ty1 = translate(x1, y1, 50, 50)
    tx2, ty2 = translate(x2, y2, 50, 50)
    pygame.draw.line(screen, WHITE, (tx1, ty1), (tx2, ty2), 2)
    # Rotated line
    angle = 45
    rx1, ry1 = rotate(x1, y1, angle)
    rx2, ry2 = rotate(x2, y2, angle)
    pygame.draw.line(screen, WHITE, (rx1, ry1), (rx2, ry2), 2)

    # Scaled line
    sx1, sy1 = scale(x1, y1, 2, 2)
    sx2, sy2 = scale(x2, y2, 2, 2)
    pygame.draw.line(screen, WHITE, (sx1, sy1), (sx2, sy2), 2)
    
    pygame.display.flip()
if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        main()


        