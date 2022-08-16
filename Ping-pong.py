from pygame import *
from random import randint
from time import time as timer
win = display.set_mode((700, 500))
background = transform.scale(image.load('ping-pong.jpg'), (700, 500))

mixer.init()
mixer.music.load('marsh.mp3')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
clock = time.Clock()
FPS = 60

font.init()
font1 = font.SysFont(None, 60)
font2 = font.SysFont(None, 150)
win1 = font1.render('Winner: Player2!', True, (0, 100, 250))
win2 = font1.render('Winner: Player1!', True, (0, 100, 250))
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
        if keys[K_s] and self.rect.y < 380:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 380:
            self.rect.y += self.speed

racket1 = Player('laser_bullet.png', 20, 200, 30, 120, 10)
racket2 = Player('laser_bullet.png', 650, 300, 30, 120, 10)
ball = GameSprite('tennis-ball2.png', 100, 300, 80, 80, 10)

speed_x = 5
speed_y = 5

run = True
finish = False
while run:
    if finish != True:
        win.blit(background, (0, 0))
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(ball, racket1) or sprite.collide_rect(ball, racket2):
            speed_x *= -1
        if ball.rect.y > 400 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            win.blit(win1, (180, 220))
        if ball.rect.x > 700:
            finish = True
            win.blit(win2, (180, 220))

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
