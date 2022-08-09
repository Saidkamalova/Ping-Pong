from pygame import *
from random import randint
from time import time as timer
win = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

mixer.init()
mixer.music.load('marsh.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60

font.init()
font1 = font.Font(None, 40)
font2 = font.Font(None, 150)
lose = font2.render('YOU LOSE!', True, (255, 0, 0))
win_text = font2.render('YOU WIN!', True, (0, 255, 0))
lost = 0
kills = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

run = True
finish = False
while run:
    win.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
