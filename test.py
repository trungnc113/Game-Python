# from os import path


# folder_of_game=path.dirname(__file__)
# print(folder_of_game)
from os import path
import pygame
pygame.init()
screen=pygame.display.set_mode((1024,768))
screen.fill((255, 255, 255))
folder_of_game=path.dirname(__file__)
image_folder = path.join(folder_of_game, 'img')
player_image = pygame.image.load(path.join(image_folder, 'tank1.png')).convert()
player_image=pygame.transform.scale(player_image,(30,30))
player_image.set_colorkey((255, 255, 255))

player_image=pygame.transform.rotate(player_image,30)
screen.blit(player_image,(100,100))

pygame.display.flip()

vector=pygame.math.Vector2
vel=vector(0,1).rotate(30)
print(vel)

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            quit()