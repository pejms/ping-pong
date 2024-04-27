from pygame import *
import time

jump = 0
fakespeed = 3
img_back = "backdrop2.jpg"
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

vremya = 10
speed_x = fakespeed
speed_y = fakespeed

start_time = time.time()
cur_time = start_time

mixer.init()
boom = mixer.Sound('otbiv.ogg')
lose = mixer.Sound('los.ogg')

font.init()
font1 = font.SysFont('Arial', 40)
font2 = font.SysFont('Arial', 25)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball2.png', 200, 200, 4, 50, 50)


game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        for i in range(10):
            vremya = vremya - 1
        window.blit(background,(0,0))
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        text = font2.render("Отскоки мяча: " + str(jump), 1, (0, 0, 0))
        text2 = font2.render("Скорость мяча: " + str(fakespeed), 1, (0, 0, 0))
        time = font1.render(str(vremya), True,(255,0,0))
        lose1 = font1.render('Левый игрок проиграл!', True,(180,0,0))
        lose2 = font1.render('Правый игрок проиграл!', True,(180,0,0))
        window.blit(text, (10, 10))
        window.blit(text2, (10, 40))
        window.blit(time, (300, 40))
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
        jump = jump + 1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        boom.play()
        speed_x *= -1
        speed_x = speed_x + 0.5
        speed_y = speed_y + 0.5
        fakespeed = fakespeed + 0.5
        jump = jump + 1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (100, 200))
    if ball.rect.x > 600:
        finish = True
        window.blit(lose2, (100, 200))
    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)