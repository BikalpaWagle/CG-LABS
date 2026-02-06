import pygame
import sys
import math

def rotate(x, y, angle, cx=0, cy=0):
    radians = math.radians(angle)
    x -= cx
    y -= cy
    x_new = x * math.cos(radians) - y * math.sin(radians)
    y_new = x * math.sin(radians) + y * math.cos(radians)
    return x_new + cx, y_new + cy

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Line with Clock")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Line points
x1, y1 = 300, 400
x2, y2 = 500, 400

cx, cy = WIDTH // 2, HEIGHT // 2
angle = 0
speed = 90 

while True:
    dt = clock.tick(60) / 1000  
    angle += speed * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)

    # Rotate line over time
    rx1, ry1 = rotate(x1, y1, angle, cx, cy)
    rx2, ry2 = rotate(x2, y2, angle, cx, cy)

    pygame.draw.line(screen, WHITE, (rx1, ry1), (rx2, ry2), 3)

    pygame.display.flip()
