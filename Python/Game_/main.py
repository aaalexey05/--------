import pygame
import random

pygame.init()

size = [800, 800]
res = [400, 400]

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, res)

clock = pygame.time.Clock()

chunk_size = 8
tile_size = 16

textures = {'0': [pygame.image.load('0.png')],
            '1': [pygame.image.load('1.png')]}


def generate_tile(x, y):
    return 1


class Chunk:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.map = [generate_tile(x, y) for y in range(
            chunk_size) for x in range(chunk_size)]

    def render(self):
        for y in range(chunk_size):
            for x in range(chunk_size):
                texture = textures[self.map[x + y * chunk_size]]
                screen.blit(texture, (self.x + x * tile_size,
                            self.y + y * tile_size))
                
chunk1 = Chunk(0, 0)

while 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    chunk1.render()

    window.blit(pygame.transform.scale(screen, size), (0, 0))
    pygame.display.update()
    clock.tick(60)
