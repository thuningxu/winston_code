import pygame
import pdb
import button

pygame.init()

screen_width = 620
screen_height = 620

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

class Player:
    def __init__(self,start,end,speed):
        self.reset(start,end,speed)

    def update(self):
        self.check_collision()
        self.grid_pos = [self.pix_pos[0] // cell_size,self.pix_pos[1] // cell_size]
        self.rect.topleft = (self.pix_pos[0] + 3,self.pix_pos[1] + 3)

    def check_collision(self):
        if self.rect.left <= 0 and self.direction == [-1,0]:
            self.direction = [0,0]
            self.rect.left = 0
        if self.grid_pos in walls:
            self.game_over = True
            self.state = 'game over'
        if self.grid_pos == self.end:
            self.game_over = True
            self.state = 'win'

##    def win_or_lose(self,state):
##        self.speed = 0
##        self.direction = [0,0]
##        if state == 'game over':
##            game_over = True
##            text = self.font.render('GAME OVER',True,(0,0,0))
##        if state == 'win':
##            text = self.font.render('YOU WIN!',True,(0,0,0))
##        screen.blit(text,(screen_width // 2 - text.get_width() // 2,155))
##
##        exit_game = self.exit_button.draw(screen)
##        restart = self.restart_button.draw(screen)
##        while not (exit_game or restart):
##            if self.restart_button.draw(screen):
##                restart = True
##            if self.exit_button.draw(screen):
##                exit_game = True
##        if restart == True:
##            self.reset()
##        if exit_game == True:
##            pygame.quit()
##            sys.exit()

    def reset(self,start,end,speed):
        self.state = 'playing'
        self.direction = [0,0]
        self.player = pygame.transform.scale(pygame.image.load('images/player.png'),(12,12))
        self.rect = self.player.get_rect()
        self.game_over = False
        self.speed = speed
        self.font = pygame.font.SysFont('PlayFair Display',100)
        self.grid_pos = start
        self.end = end
        self.pix_pos = (self.grid_pos[0] * cell_size,self.grid_pos[1] * cell_size)
        self.exit_button = button.Button(screen_width // 2,500,pygame.image.load('images/exit_btn.png'),1)
        self.restart_button = button.Button(screen_width // 2,400,pygame.image.load('images/restart_btn.png'),2)

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
        screen.blit(self.player,self.rect)
        pygame.draw.rect(screen,(0,255,0),self.rect,2)

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

run = True
while run:
    if player.game_over:
        player.speed = 0
        player.direction = [0,0]
        if player.state == 'game over':
            text = player.font.render('GAME OVER!',True,(0,0,0))
        if player.state == 'win':
            text = player.font.render('YOU WIN!',True,(0,0,0))
        screen.blit(text,(screen_width // 2 - text.get_width() // 2,155))
        if player.restart_button.draw(screen):
            print('restart')
            #player.reset()
        if player.exit_button.draw(screen):
            print('exit')
            run = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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

pygame.quit()
