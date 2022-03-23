import pygame,sys,pymunk
from random import randint

def create_apple(space,pos):
    body = pymunk.Body(999999999999999999999999999999999999999999999999999999999999*9999999999999999999999999999999999999999999999999999999999\
        ,99999999999999999999999999999999999999999999999999999999999999999*99999999999999999999999999999999999999999999999999999999999999\
        ,body_type = pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body,30)
    space.add(body,shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        screen.blit(apple_surface,apple_rect)

def static_ball(space,pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,25)
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),25)

pygame.init()
screen = pygame.display.set_mode((450,450))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (randint(-1000,1000),randint(-1000,1000))
apple_surface = pygame.transform.scale2x(pygame.image.load('snake/snake-in-pygame/images/apple.png'))
apples = []
balls = []
for x in range(350):
    balls.append(static_ball(space,(x,460)))

for x in range(350):
    balls.append(static_ball(space,(x,-10)))

for x in range(348):
    balls.append(static_ball(space,(-10,x + 1)))

for x in range(348):
    balls.append(static_ball(space,(460,x + 1)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))

    screen.fill((217,217,217))
    draw_apples(apples)
    draw_static_ball(balls)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
