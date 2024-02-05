import pygame
from setting import *
from sprites import *

vector=pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):
        self.groups=game.all_sprites #nhóm các hình ảnh
        pygame.sprite.Sprite.__init__(self,self.groups) #gọi constructor của class cha
        self.game=game
        self.image=game.player_image #hình ảnh xe tank
        self.rect=self.image.get_rect() #khung xe tank
        self.vel=vector(0,0) #vận tốc của xe
        self.position=vector(x,y)*SQSIZE
        self.rot=0 #độ xoay của xe

    def keys(self):
        self.rotation_speed=0 #tốc độ xoay của xe
        self.vel=vector(0,0)
        keys_state=pygame.key.get_pressed() #lấy giá trị boolean của tất cả các phím
        if keys_state[pygame.K_LEFT]:
            self.rotation_speed=+RotationSpeedOfPlayer
        if keys_state[pygame.K_RIGHT]:
            self.rotation_speed=-RotationSpeedOfPlayer
        if keys_state[pygame.K_UP]:
            self.vel=vector(0,playerSpeed).rotate(-self.rot) #vector di chuyển theo trục Y, theo hướng đã xoay
        if keys_state[pygame.K_DOWN]:
            self.vel=vector(0,-playerSpeed/2).rotate(-self.rot)
    def update(self):
        self.keys()
        self.rot=(self.rot+ self.rotation_speed*self.game.changing_time)%360 #độ xoay = (độ xoay hiện tại + tốc độ xoay * thời gian trôi qua kể từ khung hình trước )%360
        self.image=pygame.transform.rotate(self.game.player_image,self.rot)
        self.position+=self.vel*self.game.changing_time
        self.rect=self.image.get_rect()
        self.rect.center=self.position
    
