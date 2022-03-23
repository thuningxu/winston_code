import pygame,sys
import pdb

pygame.init()

screen_width = 620
screen_height = 620

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

class Player:
    def __init__(self,start,end,speed):
        self.direction = [0,0]
        self.speed = speed
        self.grid_pos = start
        self.player = pygame.image.load('pl')
        self.pix_pos = (self.grid_pos[0] * cell_size,self.grid_pos[1] * cell_size)

    def update(self):
        self.grid_pos = [self.pix_pos[0] // cell_size,self.pix_pos[1] // cell_size]

    def move(self):
        self.update()
        if self.direction == [1,0]:
            self.pix_pos = (self.pix_pos[0] + self.speed,self.pix_pos[1])
        if self.direction == [-1,0]:
            self.pix_pos = (self.pix_pos[0] - self.speed,self.pix_pos[1])
        if self.direction == [0,1]:
            self.pix_pos = (self.pix_pos[0],self.pix_pos[1] + self.speed)
        if self.direction == [0,-1]:
            self.pix_pos = (self.pix_pos[0],self.pix_pos[1] - self.speed)

    def draw(self):
        pygame.draw.circle(screen,(0,0,255),(self.pix_pos[0] + 10,self.pix_pos[1] + 10),6)

cell_size = 20
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0],
    [1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

walls = []
for row_index,row in enumerate(maze):
    for col_index,col in enumerate(row):
        if col == 1:
            walls.append([col_index,row_index])

start = [0,5]
end = [13,30]

player = Player(start,end,2)

def draw_maze():
    for block in walls:
        block_rect = pygame.Rect(block[0] * cell_size,block[1] * cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(255,0,0),block_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.direction = [0,-1]
            if event.key == pygame.K_DOWN:
                player.direction = [0,1]
            if event.key == pygame.K_LEFT:
                player.direction = [-1,0]
            if event.key == pygame.K_RIGHT:
                player.direction = [1,0]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.direction = [0,0]
            if event.key == pygame.K_DOWN:
                player.direction = [0,0]
            if event.key == pygame.K_LEFT:
                player.direction = [0,0]
            if event.key == pygame.K_RIGHT:
                player.direction = [0,0]

    screen.fill('white')
    draw_maze()
    player.move()
    player.draw()
    pygame.display.update()
    clock.tick(60)
