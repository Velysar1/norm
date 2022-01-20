import pygame as pg

pg.init()

class OurSprites(pg.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load('python.jpg'), (65, 65))
        self.rect = self.rect.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    
    def reset(self):
        win.blit(self image, (self.rect.x, self.rect.y))


win = pg.display.set_mode((700,500))
pg.display.set_caption('Догонялки')
clock = pg.time.Clock()
back = pg.transform.scale(pg.image.load('python.jpg'), (700, 500))

#Музыка
#pg.mixer.music.load('Название')
#pg.mixer.music.play()

#cat = OurSprites(200, 200, "Название", 10)

game_over = True
while game_over:
    win.blit(back, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_over = False
    pg.display.update()
    clock.tick(60)