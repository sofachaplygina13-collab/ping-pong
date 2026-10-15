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
    def update():
        self.rect.y+=self.speed
        self.rect.x+=self.speed
        if self.rect.y==450:
            self.rect.y+=self.speed*-1
        if self.rect.x==650:
            self.rect.x+=self.speed*-1
        

run=True
while run:
    clock.tick(FPS)

    for e in event.get():
        if e.type==QUIT:
            run=False

    
    display.update()
    window.fill((175, 238, 238))