import pygame as pg
class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))
pg.init()
run = True
win_x, win_y = 800, 480
dx=20
dy=20
screen = pg.display.set_mode((win_x, win_y))
firstObject = Rectangle(dx,dy,100,100) # สร้าง Object จากคลาส Rectangle ขึ้นมา
firstObject.draw(screen)
while(run):
    screen.fill((255, 255, 255))
    for event in pg.event.get():  
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d: #ปุ่มถูกปล่อยและเป็นปุ่ม A
                dx+=10   
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            dx-=10
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            dy+=10
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            dy-=10
        pg.draw.rect(screen,(0,20,220),(dx,dy,100,100))      
        pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()