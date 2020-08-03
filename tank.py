import pygame
from pygame.locals import *
import sys
from tank_sprites import *
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.key.set_repeat(400, 30)
clock = pygame.time.Clock()
# 初始分數為 0
score = 0

# 建立 sprite 群組，方便操作
all_sprites_group = pygame.sprite.Group()
tank_bricks_group = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()

tank = Tank('player1_U.png')
all_sprites_group.add(tank)
tank_bricks_group.add(tank)



for i in range(40):
    for j in range(30):

        if Map[j][i] == 1:
            brick = Brick('brick.jpg', (i)*BRICK_WIDTH , (j)*BRICK_HEIGHT )
            all_sprites_group.add(brick)
            bricks_group.add(brick)
            tank_bricks_group.add(brick)

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                # 左鍵按下玩家向左移動
                tank.move_left()
            elif event.key == K_RIGHT:
                # 右鍵按下玩家向右移動
                tank.move_right()
            elif event.key == K_UP:
                tank.move_up()
            elif event.key == K_DOWN:
                tank.move_down()


    window.fill((0, 0, 0))
    


    all_sprites_group.draw(window)
    all_sprites_group.update()
    clock.tick(60)
    pygame.display.flip()

