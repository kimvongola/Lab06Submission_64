import sys 
import pygame as pg

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(255,0,0),(self.x,self.y,self.w,self.h))
class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    def isMouseOn(self):
        if (20,20)<=pg.mouse.get_pos() and pg.mouse.get_pos()<=(120,120):
            return True
        else :
            return False
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
btn = Button(20,20,100,100) # สร้าง Object จากคลาส Button ขึ้นมา
while(run):
    screen.fill((255, 255, 255))
    if pg.mouse.get_pressed()[0] and btn.isMouseOn()==True:
        pg.draw.rect(screen,(204,0,204),(20,20,100,100))
    elif btn.isMouseOn()==True:
        pg.draw.rect(screen,(80,80,80),(20,20,100,100)) 
    else :
        btn.draw(screen)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False