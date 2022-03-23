import pygame, sys

screen = pygame.display.set_mode((500,500))

class myclass(pygame.sprite.Sprite):
    def __init__(self):
        #super().__init__(self)
        self.group = pygame.sprite.Group()
        self.group.add('lol')

myclass = myclass()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
