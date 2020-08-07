import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 640,672

BRICK_WIDTH, BRICK_HEIGHT = 24,24
# 坦克大小
TANK_WIDTH, TANK_HEIGHT = 40, 40
# 坦克移動的速度
TANK_SPEED = 5


Map = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0],
[0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

class Tank_Sprite(pygame.sprite.Sprite):
    def __init__(self,image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/" + image_file).convert()
        # 設定透明的 colorkey, 如果圖片的顏色與 colorkey 所指定的顏色相同則會顯示成透明
        # 目前是圖片中黑色的部分會顯示成透明
        self.image.set_colorkey((0, 0, 0))
        # 物件的 rect(長方形) 以圖片的長寬來定義
        self.rect = self.image.get_rect()

class Brick(Tank_Sprite):
    # 由於磚塊初始化位置不同, 所以另外傳入初始化位置
    def __init__(self, image_file, x, y):
    # 設定磚塊位置
        Tank_Sprite.__init__(self, image_file)
        self.rect.left, self.rect.top = x, y

class Grass(Tank_Sprite):
    def __init__(self, image_file, x, y):
    # 設定磚塊位置
        Tank_Sprite.__init__(self, image_file)
        self.rect.x, self.rect.y = x, y

class Bullet(Tank_Sprite):
    def __init__(self):
        Tank_Sprite.__init__(self, "bullet_up.png")
        self.image_up =  pygame.image.load("images/bullet_up.png").convert()
        self.image_down =  pygame.image.load("images/bullet_down.png").convert()
        self.image_left =  pygame.image.load("images/bullet_left.png").convert()
        self.image_right =  pygame.image.load("images/bullet_right.png").convert()
        self.image_up.set_colorkey((255, 255, 255))
        self.image_down.set_colorkey((255, 255, 255))
        self.image_left.set_colorkey((255, 255, 255))
        self.image_right.set_colorkey((255, 255, 255))
        self.dir_x, self.dir_y = 0, 0
        self.speed = 6
        self.life = False
    def changeDir(self, x, y):
        self.image.set_colorkey((255, 255, 255))
        if x == 0 and y == -1:
            self.dir_x, self.dir_y = x,y
            self.image = self.image_up
        elif x == 0 and y == 1:
            self.dir_x, self.dir_y = x,y
            self.image = self.image_down
        elif x == 1 and y == 0:
            self.dir_x, self.dir_y = x,y
            self.image = self.image_right
        elif x == -1 and y == 0:
            self.dir_x, self.dir_y = x,y
            self.image = self.image_left
    def move(self):
        self.rect.move_ip(self.speed * self.dir_x, self.speed * self.dir_y)


class Tank(Tank_Sprite):
    def __init__(self, image_file):
        Tank_Sprite.__init__(self, image_file)
        self.rect.bottom = WINDOW_HEIGHT
        self.rect.left = (WINDOW_WIDTH - self.image.get_width()) / 2
        self.dir_x, self.dir_y = 0, -1
        self.bullet = Bullet()
    def move_up(self, brick_sprites):
        self.dir_x, self.dir_y = 0, -1
        # 設定坦克圖片
        self.image = pygame.image.load("images/Tank.png").convert()
        self.image.set_colorkey((0, 0, 0))
        # 往上移動
        self.rect.move_ip(0,-TANK_SPEED)
        # 如果坦克還沒碰到上面邊界
        if self.rect.top > 0:
            # 判斷是否移動後碰撞
            if pygame.sprite.spritecollide(self, brick_sprites, False):
                # 如果碰撞到磚塊則移回原位
                self.rect.move_ip(0, TANK_SPEED)

    def move_down(self,brick_sprites):
        self.dir_x, self.dir_y = 0, 1
        # 如果坦克還沒碰到下面邊界
        self.image = pygame.image.load("images/Tank_D.png").convert()
        self.image.set_colorkey((0, 0, 0))
        if self.rect.bottom < WINDOW_HEIGHT:
            # 往下移動
            self.rect.move_ip(0,TANK_SPEED)
            # 判斷是否移動後碰撞
            if pygame.sprite.spritecollide(self, brick_sprites, False):
                # 如果碰撞到磚塊則移回原位
                self.rect.move_ip(0, -TANK_SPEED)
    
    def move_left(self,brick_sprites):
        self.dir_x, self.dir_y = -1, 0
        self.image = pygame.image.load("images/Tank_L.png").convert()
        self.image.set_colorkey((0, 0, 0))
        # 如果坦克還沒碰到左邊邊界
        if self.rect.left > 0:
            # 往左移動
            self.rect.move_ip(-TANK_SPEED, 0)
            # 判斷是否移動後碰撞
            if pygame.sprite.spritecollide(self, brick_sprites, False):
                # 如果碰撞到磚塊則移回原位
                self.rect.move_ip(TANK_SPEED, 0)
    def move_right(self,brick_sprites):
        self.dir_x, self.dir_y = 1, 0
        self.image = pygame.image.load("images/Tank_R.png").convert()
        self.image.set_colorkey((0, 0, 0))
        # 如果坦克還沒碰到右邊邊界
        if self.rect.right < WINDOW_WIDTH:
            # 往右移動
            self.rect.move_ip(TANK_SPEED, 0)
            # 判斷是否移動後碰撞
            if pygame.sprite.spritecollide(self, brick_sprites, False):
                # 如果碰撞到磚塊則移回原位
                self.rect.move_ip(-TANK_SPEED,0)

    def fire(self):
        # 發射子彈
        self.bullet.changeDir(self.dir_x, self.dir_y)
        self.bullet.life = True


        if self.dir_x == 0 and self.dir_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top + 1
        elif self.dir_x == 0 and self.dir_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom - 1
        elif self.dir_x == -1 and self.dir_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.dir_x == 1 and self.dir_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20
        



