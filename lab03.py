# def bresenham(x1,y1,x2,y2):
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)

#     if(x2>x1):
#         lx=1
#     else:
#         lx=-1
#     if(y2>y1):
#         ly=1
#     else:
#         ly=-1

#     x=x1
#     y=y1

    
#     if(dx>dy):
#         P=2*dy-dx
    
#         for i in range(dx+1):
#             print(x,y)
#             if(P<0):
#                 x=x+lx
#                 P=P+2*dy
#             else:
#                 x=x+lx
#                 y=y+ly
#                 P=P+2*dy-2*dx
    
#     else:
#         P=2*dx-dy
        
#         for i in range(dy+1):
#             if(P<0):
#                 y=y+ly
#                 P=P+2*dx
#             else:
#                 x=x+lx
#                 y=y+ly
#                 P=P+2*dx+2*dy
# x1=int(input("Enter the value of x1:"))
# y1=int(input("Enter the value of y1:"))
# x2=int(input("Enter the value of x2:"))
# y2=int(input("Enter the value of y2:"))

# bresenham(x1,y1,x2,y2)
import pygame
import sys
pygame.init()
w,h=1000,800
screen=pygame.display.set_mode((w,h))
White=(255,255,255)
Black=(0,0,0)

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
            screen.set_at((x,y),White)
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
            screen.set_at((x,y),White)    

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(Black)
    # bresenham(0,0,100,300)      
    


    bresenham(300,100,100,700)  
    bresenham(20,300,600,300)  
    bresenham(300,100,500,700)  
    bresenham(100,700,600,300)
    bresenham(20,300,500,700)

    pygame.display.flip()
                



