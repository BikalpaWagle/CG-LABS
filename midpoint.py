import pygame
import sys
pygame.init()
w,h=1000,1000
screen=pygame.display.set_mode((w,h))
white=(255,255,255)
Black=(0,0,0)   
def mid(xc,yc,r):

    x=0
    y=r
    d=1-r

    while(x<y):
        screen.set_at((xc+x, yc+y), white)
        screen.set_at((xc-x, yc+y), white)
        screen.set_at((xc+x, yc-y), white)
        screen.set_at((xc-x, yc-y), white)
        screen.set_at((xc+y, yc+x), white)
        screen.set_at((xc-y, yc+x), white)
        screen.set_at((xc+y, yc-x), white)
        screen.set_at((xc-y, yc-x), white)
        x=x+1
        if(d<0):
           
            d=d+2*x+1

        else:
            y=y-1
            d=d+2*x-2*y+1
def mid2(xc,yc,r):
    x=0
    y=r
    d=1-r

    while(x<y):
        screen.set_at((xc+x, yc+y), white)
        screen.set_at((xc-x, yc+y), white)
        screen.set_at((xc+y, yc+x), white)
        screen.set_at((xc-y, yc+x), white)
    
        
        x=x+1
        if(d<0):
           
            d=d+2*x+1

        else:
            y=y-1
            d=d+2*x-2*y+1


def bresenham(x1,y1,x2,y2):
    dx=abs(x2-x1)
    dy=abs(y2-y1)

    if(x2>x1):
        lx=1
    else:
        lx=-1
    if(y2>y1):
        ly=1
    else:
        ly=-1

    x=x1
    y=y1

    
    if(dx>dy):
        P=2*dy-dx
    
        for i in range(dx):
            if(P<0):
                x=x+lx
                P=P+2*dy
            else:
                x=x+lx
                y=y+ly
                P=P+2*dy-2*dx
            screen.set_at((x,y),white)
    else:
        P=2*dx-dy
        
        for i in range(dy):
            if(P<0):
                y=y+ly
                P=P+2*dx
            else:
                x=x+lx
                y=y+ly
                P=P+2*dx+2*dy
            screen.set_at((x,y),white) 

   
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(Black)
    # mid(500,500,250)
    # mid(400,350,25)
    # mid(600,350,25) 
    # mid2(500,550,100)

    mid(250,250,125)
    mid(200,175,12)
    mid(300,175,12) 
    mid2(250,275,50)
    bresenham(250,375,250,700)
    bresenham(250,450,400,400)
    bresenham(250,450,100,400)
    bresenham(250,700,400,900)
    bresenham(250,700,100,900)
    
    


    pygame.display.flip()
                

                    


