# x1=int(input("Enter x1"))
# y1=int(input("Enter y1"))
# x2=int(input("Enter x2"))
# y2=int(input("Enter y2"))
# dx=abs(x2-x1)
# dy=abs(y2-y1)
# if(dx>dy):
#     step=dx
# else:
#     step=dy
# xinc=dx/step
# yinc=dy/step
# x=x1
# y=y1

# for i in range(0,step+1):
#     print (x,y)
#     x=x+xinc
#     y=y+yinc
    
import pygame
import sys
pygame.init()
w,h=1000,800
screen=pygame.display.set_mode((w,h))
White=(255,255,255)
Black=(0,0,0)

def drawing_line(x1,y1,x2,y2):
# x1=int(input("Enter x1"))
# y1=int(input("Enter y1"))
# x2=int(input("Enter x2"))
# y2=int(input("Enter y2"))
    dx=(x2-x1)
    dy=(y2-y1)
    if(abs(dx)>abs(dy)):
        step=abs(dx)
    else:
        step=abs(dy)
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1

    for i in range(0,step+1):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),White)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(Black)
        
    drawing_line(1500,500,2500,1000)
    drawing_line(2500,1000,2500,2000)
    drawing_line(2500,2000,1750,2000)
    drawing_line(1750,2000,1750,1500)
    drawing_line(1750,1500,1250,1500)
    drawing_line(1250,1500,1250,2000)
    drawing_line(1250,2000,500,2000)
    drawing_line(500,2000,500,1000)
    drawing_line(750,1250,1000,1250)
    drawing_line(1000,1250,1000,1500)
    drawing_line(1000,1500,750,1500)
    drawing_line(750,1500,750,1250)
    drawing_line(2000,1250,2250,1250)
    drawing_line(2250,1250,2250,1500)
    
    pygame.display.flip()       

