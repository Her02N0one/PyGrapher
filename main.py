import pygame
from math import cos

WIDTH, HEIGHT = (512, 512)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

x_offset = WIDTH // 2
y_offset = HEIGHT // 2
x = -x_offset


class Graph:
    def __init__(self, width, height):
        self.graph_surface = pygame.Surface((width, height))
        self.points = list()

    def fill(self, color: tuple):
        self.graph_surface.fill(color)


def line(x):
    y = int(cos(x) * 0.1)
    return y


def parabola(x):
    y = (x**2) // 1000
    return y


def absolute(x):
    y = abs(x)
    return y

def reset(screen):
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (x_offset, 0), (x_offset, HEIGHT))
    pygame.draw.line(screen, (0, 0, 0), (0, y_offset), (WIDTH, y_offset))


reset(screen)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if x <= WIDTH:
    #     pygame.draw.circle(screen, (0, 0, 0), (x + x_offset, -line(x) + y_offset), 0)
    #     x += 1

    pygame.display.flip()
