from pygame import *

class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
 
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #метод, отрисовывающий героя на окне
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс главного игрока
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 430:
           self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 430:
            self.rect.y += self.speed

window = display.set_mode((700,500))
window.fill((255, 250, 112))




clock = time.Clock()
FPS = 60
game = True
platform_l = Player("platform_l.png", 10,200, 20, 70, 10)
platform_r = Player("platform_r.png", 670, 200, 20, 70, 10)
big_ball = GameSprite("ball.png", 300, 200, 50, 50, 10)

mixer.init()
mixer.music.load('untilted.ogg')
mixer.music.play()

stolknovenie = mixer.Sound('stolk.ogg')
speed_x = 3
speed_y = 3
font.init()
font1 = font.SysFont('Arial', 35)
lose1 = font1.render("player 1 lox", True, (180, 0, 0))
lose2 = font1.render("player 2 lox", True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    big_ball.rect.x += speed_x
    big_ball.rect.y += speed_y
    if big_ball.rect.y > 450 or big_ball.rect.y < 0:
        speed_y *= -1
    if big_ball.rect.x < 0:
        window.blit(lose1, (200,200))
        display.update()
        time.wait(3000)
        game = False
    if big_ball.rect.x > 650:
        window.blit(lose2, (200,200))
        display.update()
        time.wait(3000)
        game = False
    if sprite.collide_rect(platform_r, big_ball) or sprite.collide_rect(platform_l, big_ball):
        speed_x *= -1
        speed_y *= -1
    
    window.fill((94, 92, 92))

    platform_l.reset()
    platform_r.reset()
    big_ball.reset()
    platform_l.update_l()
    platform_r.update_r()


    display.update()
    clock.tick(FPS)