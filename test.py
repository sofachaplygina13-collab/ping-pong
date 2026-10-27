from pygame import *
from random import randint

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
            self.speed_y=randint(5,10)
            self.speed_y*=-1
        if self.rect.x>=650:
            self.speed_x*=-1
        if self.rect.y<=0:
            self.speed_y=-(randint(5,10))
            self.speed_y*=-1
        if self.rect.x<=0:
            self.speed_x*=-1
    def restart(self):
        self.rect.x=325
        self.rect.y=225
        
class Racket(GameSprite):
    def __init__(self,name,speed,x,y,width,height):
        super().__init__(name,speed,x,y,width,height)
    def update(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_UP] and self.rect.y>0:
            self.rect.y-=self.speed
        if key_pressed[K_DOWN] and self.rect.y<300:
            self.rect.y+=self.speed
    def update1(self):
        key_pressed=key.get_pressed()
        if key_pressed[K_w] and self.rect.y>0:
            self.rect.y-=self.speed
        if key_pressed[K_s] and self.rect.y<300:
            self.rect.y+=self.speed

ball=Ball('i.png',7,325,225,75,50)
player1=Racket('r.png',5,10,75,55,200)
player2=Racket('r.png',5,650,75,55,200)

font.init()
font=font.Font(None,100)
l=0
r=0
count=font.render(str(l)+':'+str(r),True,(250,1,4))
win1=font.render('Победа игрок1',True,(250,100,4))
win2=font.render('Победа игрок2',True,(250,100,4))

number=0
finish=1
run=True
while run:
    clock.tick(FPS)

    for e in event.get():
        if e.type==QUIT:
            run=False

       
    window.fill((175, 238, 238))   
    window.blit(count,(300,0))
    ball.reset()
    player1.reset()
    player2.reset()
    player1.update1()
    player2.update()  
    if l>=10:
        window.blit(win1,(100,220))
    if r>=10:
        window.blit(win2,(100,220))

    if finish==0:  
        ball.update()  

        if sprite.collide_rect(ball,player1):
            ball.speed_x=-(randint(5,10))
            ball.speed_x*=-1
        if sprite.collide_rect(ball,player2):
            ball.speed_x=randint(5,10)
            ball.speed_x*=-1

        if ball.rect.x>=650:
            ball.restart()
            l+=1
            count=font.render(str(l)+':'+str(r),True,(250,1,4))
            finish=1
        if ball.rect.x<=0:
            ball.restart()
            r+=1
            count=font.render(str(l)+':'+str(r),True,(250,1,4))
            finish=1

        if l>=10:
            finish=2
        if r>=10:
            finish=2
    else:
        number+=1
        if finish==1 and number==100:
            finish=0
            number=0
        if finish==2 and number==100:
            l=0
            r=0
            count=font.render(str(l)+':'+str(r),True,(250,1,4))
            finish=0
            number=0
    
    display.update()
    
