from pygame import *
import random
import time as t

class Sprit(sprite.Sprite):
    def __init__(self, n_img, w, h, speed, x, y, hi, wi):
        super().__init__()
        self.pic = transform.scale(image.load(n_img),(w,h))
        self.rect = self.pic.get_rect()
        self.rect.x, self.rect.y, = x, y
        self.speed = speed
        self.hi = hi
        self.wi = wi
    
    def upd(self):
        win.blit(self.pic,(self.rect.x, self.rect.y))

    

class Player(Sprit):
    def ev(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >= 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <= self.wi-10:
            self.rect.x += self.speed

class Enemy(Sprit):
    def mov(self):
        xy = random.choice([self.rect.x,self.rect.y])
        lr = random.choice(['l','r'])
        if xy == self.rect.x :
            if lr == 'l'and self.rect.x >= 10:
                for i in range(random.randint(10,100)):
                    self.rect.x -= self.speed
            elif lr == 'r'and self.rect.x <= self.wi-10:
                for i in range(random.randint(10,100)):
                    self.rect.x += self.speed
           
    
class Wall(sprite.Sprite):
    def __init__(self, w, h, r, g, b, x, y):
        super().__init__()
        self.pic = Surface((w,h))
        self.pic.fill((r,g,b))
        self.rect = self.pic.get_rect()
        self.rect.x, self.rect.y = x, y

    def draw(self):
        win.blit(self.pic,(self.rect.x, self.rect.y))

winh = 800
winw = 600
fps = 25
kos = 'png.png'
mixer.init()
mixer.music.load('bensound-dubstep.mp3')
mixer.music.set_volume(0.1)
mixer.music.play()

win = display.set_mode((winh,winw))
timer = time.Clock()
bg = transform.scale(image.load(kos),(winh,winw))
new = image.load('new.jpg')
wl = Wall(20, 200, 100, 200, 20,  random.randint(100,700),  0)
wl1 = Wall(20, 200, 100, 200, 20,  random.randint(100,700),  400)
wl3 = Wall(3000, 20, 100, 200, 20, 0,  0)
wl4 = Wall(3000, 20, 100, 200, 20, 0,  580)

game = True

pl = Player('png.png',int(winw/5),int(winh/5),10,400,400,winh,winw)
en = Enemy('png.png',int(winw/5),int(winh/5),1,400,50,winh,winw)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        win.fill((100,50,5))
        win.blit(bg,(0,0))
        en.upd()
        en.mov()
        pl.upd()
        pl.ev()
        display.update()
        timer.tick(60)