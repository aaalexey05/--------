import pygame
import random
from PIL import Image

pygame.init()

size = [800, 800]
res = [400, 400]

cam_x, cam_y = 0, 0

window = pygame.display.set_mode(size)
screen = pygame.transform.scale(window, res)

clock = pygame.time.Clock()

chunk_size = 8
tile_size = 16

textures = {0: [pygame.image.load('0.png')],
            1: [pygame.image.load('1.png')]}

world_size_chunk_y = 1024 // chunk_size
world_size_chunk_x = 1024 // chunk_size

world_map = Image.open('world.png').load()


def chunks_on_screen():
    x1 = cam_x // (chunk_size * tile_size)
    y1 = cam_y // (chunk_size * tile_size)

    x2 = (cam_x + res[0]) // (chunk_size * tile_size)
    y2 = (cam_y + res[1]) // (chunk_size * tile_size)

    x1 = min(max(x1, 0), world_size_chunk_x - 1)
    x2 = min(max(x2, 0), world_size_chunk_x - 1)

    y1 = min(max(y1, 0), world_size_chunk_y - 1)
    y2 = min(max(y2, 0), world_size_chunk_y - 1)

    result = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            result.append(x + y * world_size_chunk_x)

    return result


def generate_tile(x, y, chunk_x, chunk_y):
    tile_x = (chunk_x // tile_size) + x
    tile_y = (chunk_y // tile_size) + y

    return int(world_map[tile_x, tile_y][0]/255 > 0.5)


class Chunk:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.map = [generate_tile(x, y, self.x, self.y) for y in range(
            chunk_size) for x in range(chunk_size)]

    def render(self):
        for y in range(chunk_size):
            for x in range(chunk_size):
                texture = textures[self.map[x + y * chunk_size]][0]
                screen.blit(texture, (self.x + x * tile_size - cam_x,
                            self.y + y * tile_size - cam_y))


chunks = []
for y in range(world_size_chunk_y):
    for x in range(world_size_chunk_x):
        chunks.append(Chunk(x * chunk_size * tile_size,
                      y * chunk_size * tile_size))

frame = 0
while 1:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        cam_x -= 1
    if key[pygame.K_d]:
        cam_x += 1
    if key[pygame.K_w]:
        cam_y -= 1
    if key[pygame.K_s]:
        cam_y += 1

    for i in chunks_on_screen():
        chunks[i].render()

    window.blit(pygame.transform.scale(screen, size), (0, 0))
    pygame.display.update()
    clock.tick(400)
    frame += 1
    if frame % 100 == 0:
        pygame.display.set_caption('FPS: ' + str(round(clock.get_fps())))
        chunks_on_screen()
