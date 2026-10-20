from pygame import *

window=display.set_mode((700,500))
window.fill((175, 238, 238))

clock=time.Clock()
FPS=60

class GameSprite(sprite.Sprite):
    def __init__(self,name,speed,x,y,width,height):
        super().__init__()
        self.image=transform.scale(image.load(name),(width,height))
        self.speed=speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Ball(GameSprite):
    def __init__(self,name,speed,x,y,width,height):
        super().__init__(name,speed,x,y,width,height)
        self.speed_y=self.speed
        self.speed_x=self.speed
    def update(self):
        self.rect.y+=self.speed_y
        self.rect.x+=self.speed_x
        if self.rect.y>=450:
            self.speed_y*=-1
        if self.rect.x>=650:
            self.speed_x*=-1
        if self.rect.y<=0:
            self.speed_y*=-1
        if self.rect.x<=0:
            self.speed_x*=-1
        
class Racket(GameSprite):
    def __init__(self,name,speed,x,y,width,height):
        super().__init__(name,speed,x,y,width,height)
    def update(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed
        if key_pressed[K_DOWN] and self.rect.y<200:
            self.rect.y+=self.speed
    def update1(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed
        if key_pressed[K_s] and self.rect.y<200:
            self.rect.y+=self.speed

ball=Ball('i.webp',10,325,225,75,50)
player1=Racket('r.webp',5,10,75,35,350)
player2=Racket('r.webp',5,650,75,35,350)
run=True
while run:
    clock.tick(FPS)

    for e in event.get():
        if e.type==QUIT:
            run=False
            
    ball.reset()
    ball.update()    
    player1.reset()
    player1.update1()
    player2.reset()
    player2.update()

    if sprite.collide_rect(ball,player1):
        ball.speed_x*=-1
        ball.rect.x+=5
    if sprite.collide_rect(ball,player2):
        ball.speed_x*=-1
        ball.rect.x-=5
    
    display.update()
    window.fill((175, 238, 238))
