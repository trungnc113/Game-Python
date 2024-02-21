from os import path
import pygame
from abc import ABC,abstractmethod
from setting import *
from sprites import *

vector=pygame.math.Vector2

class Player(pygame.sprite.Sprite,ABC):
    def __init__(self,game,x,y,image):
        self.groups=game.all_sprites #nhóm các hình ảnh
        #super().__init__(self.groups)
        pygame.sprite.Sprite.__init__(self,self.groups) #gọi constructor của class cha
        self.game=game
        self.image_player=getImageTank(image)
        self.image=self.image_player
        self.rect=self.image.get_rect() #khung xe tank
        self.vel=vector(0,0) #vận tốc của xe
        self.position=vector(x,y)*SQSIZE
        self.rot=0 #độ xoay của xe
        self.last_fire=0
        self.rotation_speed=0

    def get_game(self):
        return self.game
    def set_rotation_speed(self, speed):
        self.rotation_speed = speed
    def get_rotation_speed(self):
        return self.rotation_speed
    def set_vel(self,vel):
        self.vel=vel
    def get_rot(self):
        return self.rot
    def get_last_fire(self):
        return self.last_fire
    def set_last_fire(self,last_fire):
        self.last_fire=last_fire
    def get_position(self):
        return self.position
    
    @abstractmethod
    def keys(self):
        pass
    # def keys(self):
    #     self.rotation_speed=0 #tốc độ xoay của xe
    #     self.vel=vector(0,0)
    #     keys_state=pygame.key.get_pressed() #lấy giá trị boolean của tất cả các phím
    #     if keys_state[pygame.K_LEFT]:
    #         self.rotation_speed=+RotationSpeedOfPlayer
    #     if keys_state[pygame.K_RIGHT]:
    #         self.rotation_speed=-RotationSpeedOfPlayer
    #     if keys_state[pygame.K_UP]:
    #         self.vel=vector(0,playerSpeed).rotate(-self.rot) #vector di chuyển theo trục Y, theo hướng đã xoay và trong pygame độ xoay dương vector quay theo chiều kim đồng hồ
    #     if keys_state[pygame.K_DOWN]:
    #         self.vel=vector(0,-playerSpeed/2).rotate(-self.rot)
    #     if keys_state[pygame.K_m]:
    #         now=pygame.time.get_ticks()
    #         if now-self.last_fire > bullet_rate:
    #             self.last_fire=now
    #             direction=vector(0,1).rotate(-self.rot)
    #             position=self.position+turret.rotate(-self.rot)
    #             Bullet(self.game,position,direction)

    def update(self):
        self.keys()
        self.rot=(self.rot+ self.rotation_speed*self.game.changing_time)%360 #độ xoay = (độ xoay hiện tại + tốc độ xoay * thời gian trôi qua kể từ khung hình trước )%360
        self.image=pygame.transform.rotate(self.image_player,self.rot) #trong pygame độ xoay dương hình quay ngược chiều kim đồng hồ
        self.position+=self.vel*self.game.changing_time
        self.rect=self.image.get_rect()
        self.rect.center=self.position
#-----------------------------------------------------------------------------------    
class Player1(Player):
    def __init__(self, game, x, y,image):
        super().__init__(game, x, y,image)

    def keys(self):
        super().set_rotation_speed(0)
        super().set_vel(vector(0,0))
        keys_state=pygame.key.get_pressed() #lấy giá trị boolean của tất cả các phím
        if keys_state[pygame.K_LEFT]:
            super().set_rotation_speed(super().get_rotation_speed()+RotationSpeedOfPlayer)
        if keys_state[pygame.K_RIGHT]:
            super().set_rotation_speed(super().get_rotation_speed()-RotationSpeedOfPlayer)
        if keys_state[pygame.K_UP]:
            super().set_vel(vector(0,playerSpeed).rotate(-super().get_rot()))  # di chuyển theo trục Y, theo hướng đã xoay và trong pygame độ xoay dương vector quay theo chiều kim đồng hồ
        if keys_state[pygame.K_DOWN]:
            super().set_vel(vector(0,-playerSpeed/2).rotate(-super().get_rot()))
        if keys_state[pygame.K_m]:
            now=pygame.time.get_ticks()
            if now-super().get_last_fire() > bullet_rate:
                super().set_last_fire(now)
                direction=vector(0,1).rotate(-super().get_rot())
                position=super().get_position()+turret.rotate(-super().get_rot())
                Bullet(super().get_game(),position,direction)
#-----------------------------------------------------------------------------------    
class Player2(Player):
    def __init__(self, game, x, y,image):
        super().__init__(game, x, y,image)

    def keys(self):
        super().set_rotation_speed(0)
        super().set_vel(vector(0,0))
        keys_state=pygame.key.get_pressed() #lấy giá trị boolean của tất cả các phím
        if keys_state[pygame.K_a]:
            super().set_rotation_speed(super().get_rotation_speed()+RotationSpeedOfPlayer)
        if keys_state[pygame.K_d]:
            super().set_rotation_speed(super().get_rotation_speed()-RotationSpeedOfPlayer)
        if keys_state[pygame.K_w]:
            super().set_vel(vector(0,playerSpeed).rotate(-super().get_rot()))  # di chuyển theo trục Y, theo hướng đã xoay và trong pygame độ xoay dương vector quay theo chiều kim đồng hồ
        if keys_state[pygame.K_s]:
            super().set_vel(vector(0,-playerSpeed/2).rotate(-super().get_rot()))
        if keys_state[pygame.K_f]:
            now=pygame.time.get_ticks()
            if now-super().get_last_fire() > bullet_rate:
                super().set_last_fire(now)
                direction=vector(0,1).rotate(-super().get_rot())
                position=super().get_position()+turret.rotate(-super().get_rot())
                Bullet(super().get_game(),position,direction)
#-----------------------------------------------------------------------------------    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,game,position,direction):
        self.groups=game.all_sprites,game.bullets
        pygame.sprite.Sprite.__init__(self,self.groups)
        self.game=game
        self.image=game.bullet_image
        self.rect=self.image.get_rect()
        self.position=position
        self.rect.center=position
        self.vel=direction*bulletSpeed
    def update(self):
        self.position+=self.vel*self.game.changing_time
        self.rect.center=self.position