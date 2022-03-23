import pygame, sys

r = 0
g = 0
b = 0
index = 0
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((244,121,131))
    if index == 0 and r != 255:
        r += 1
        index += 1
    else:
        r = 0
        index += 1
    if index == 1 and g != 255:
        g += 1
        index += 1
    else:
        g = 0
        index += 1
    if index == 2 and b != 255:
        b += 1
        index = 0
    else:
        b = 0
        index = 0

    pygame.display.update()
    clock.tick(60)
