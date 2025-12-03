from pygame import *
win = display.set_mode((500, 500))
win.fill((255, 255, 255))
FPS = 60
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed


player_left = Player('racket.png', 30, 200, 20, 70, 5)
player_right = Player('racket.png', 450, 200, 20, 70, 5)
ball = GameSprite('tenis_ball.png', 250, 250, 50, 50, 6)

speed_x = 3
speed_y = 2
finish = False
while finish == False:
    for e in event.get():
        if e.type == QUIT:
            finish = True
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.x >= 450 or ball.rect.x <= 0:
        speed_x *= -1
    if ball.rect.y >= 450 or ball.rect.y <= 0:
        speed_y *= -1

    if sprite.collide_rect(player_left, ball):
        
        speed_x *= -1
    if sprite.collide_rect(player_right, ball):
        
        speed_x *= -1


    win.fill((255, 255, 255))
    player_left.update_l()
    player_right.update_r()
    player_left.reset()
    player_right.reset()
    ball.reset()
    display.update()
    clock.tick(FPS)



