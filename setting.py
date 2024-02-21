from os import path
import pygame
vector=pygame.math.Vector2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (120, 120, 120)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (120, 104, 82)
BLUE = (0, 0, 255)

WIDTH=1024  
HEIGHT=768
FPS=60
TITLE='TANK TROUBLE'
BGCOLOR=WHITE   

SQSIZE=16 #KÍCH THƯỚC 1 Ô LƯỚI TRONG GAME
GRIDWIDTH=WIDTH/SQSIZE #SỐ Ô THEO CHIỀU RỘNG
GRIDHEIGHT=HEIGHT/SQSIZE #SỐ Ô THEO CHIỀU CAO

playerSpeed=200


PLAYER_IMAGE1='tank1.png'
PLAYER_IMAGE2='tank2.jpg'


RotationSpeedOfPlayer=120

player_box=pygame.Rect(0,0,25,28)

#shooting setting
BULLET_IMAGE='BULLET.png'
bulletSpeed=500
bullet_rate=700
turret=vector(0,25)

def getImageTank(image):
    folder_of_game=path.dirname(__file__) #tạo đường dẫn đến thư mục chứa tệp chỉ định
    image_folder = path.join(folder_of_game, 'img') #kết hợp thành đường dẫn đến thư mục img trong folder chưa tệp đang chạy
    player_image = pygame.image.load(path.join(image_folder, image)).convert() #kết hợp tạo thành đường dẫn đến file ảnh chuyển đổi hình ảnh thành dạng pixel phù hợp với màn hình
    player_image=pygame.transform.scale(player_image,(30,30))
    player_image.set_colorkey(WHITE)
    return player_image