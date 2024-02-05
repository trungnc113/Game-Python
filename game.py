from os import path
import pygame
from setting import *
from sprites import *
class Game:
    def __init__(self):
        pygame.init()#khởi tạo pygame
        #pygame.mixer.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock=pygame.time.Clock()
        pygame.display.set_caption(TITLE)
        self.data()
    def data(self):
        folder_of_game=path.dirname(__file__) #tạo đường dẫn đến thư mục chứa tệp chỉ định
        image_folder = path.join(folder_of_game, 'img') #kết hợp thành đường dẫn đến thư mục img trong folder chưa tệp đang chạy
        self.player_image = pygame.image.load(path.join(image_folder, PLAYER_IMAGE)).convert() #kết hợp tạo thành đường dẫn đến file ảnh chuyển đổi hình ảnh thành dạng pixel phù hợp với màn hình
        self.player_image=pygame.transform.scale(self.player_image,(70,70))
        self.player_image.set_colorkey(WHITE)
    def run(self):
        self.playing=True
        while self.playing:
            self.changing_time=self.clock.tick(FPS)/1000 #tính thời gian trôi qua kể từ khung hình trước(giây)
            self.events()
            self.update()
            self.draw()
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    def quit(self):
        pygame.quit()
        quit()
    def new(self):
        self.all_sprites=pygame.sprite.Group()
        self.player=Player(self,10,10)
    def update(self):
        self.all_sprites.update()
    def events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                self.quit()
    
g=Game()
while True:
    g.new()
    g.run()
