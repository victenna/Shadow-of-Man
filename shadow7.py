import pygame#,math
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([1275,800])
background1=pygame.image.load('background1.png')
background_rect=background1.get_rect(center=(638,400))
rate=pygame.image.load('rate1.png')
images=[]
images1=[0]*11
for i in range (11):
    #images.append(pygame.image.load('post.png'))
    
    images.append(pygame.image.load('man'+str(i)+'.png'))
    images[i]=pygame.transform.scale(images[i],(100,190))
    images1[i]=pygame.transform.flip(images[i],True,False)


h=190
H=525
X0,Y0=100,150
Y1=Y0+H
L0=420

X0pipe=X0+L0
Y0pipe=495
class Pipe():
    def __init__(self):
        self.image=images[0]
        self.rect=self.image.get_rect()
        self.rect.left=X0pipe
        self.rect.top=Y0pipe
        self.k,self.k1=0,0
        self.dx=5
        self.q=1
    def motion(self):
        self.k+=1
        self.k1=self.k%10
        print('k=',self.k)
        if self.k<=65:
            self.rect.left+=self.dx
            self.image=images[self.k1]
        if self.k>65:
            self.rect.left-=self.dx
            self.image=images1[self.k1]
        if self.k>130:
            self.rect.left+=self.dx
            self.image=images[self.k1]
            self.k=0
    def shadow1(self):
        Point3=(self.rect.left+50,Y0pipe)
        Point2=(X0,Y0pipe)
        #pygame.draw.line(screen,'black',Point2,Point3,10)
    def shadow(self):
        #Point6=(self.rect.left+50,675)
        Point6=(self.rect.left,675)
        Point5=((self.rect.left)+(self.rect.left-X0)*h/(H-h),675)
        pygame.draw.line(screen,'brown',Point6,Point5,10)
        pygame.draw.circle(screen,'brown',Point5,20)
        
    def white_line(self):
        Point1=(X0,Y0)
        Point5=((self.rect.left)+(self.rect.left-X0)*h/(H-h),675)
        pygame.draw.line(screen,'white',Point1,Point5,2)
    def draw(self):
        screen.blit(self.image,self.rect)

man=Pipe()
Point1=(X0,Y0)
Point2=(X0,Y0+H-h)
Point4=(X0,Y0+H)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(background1,background_rect)
    screen.blit(rate,(500,50))
    #pygame.draw.circle(screen,'red',Point1,5)
    #pygame.draw.line(screen,'green',Point1,Point2,10)
    #pygame.draw.line(screen,'red',Point2,Point4,10)
    man.motion()
    man.shadow()
    man.white_line()
    man.draw()
    pygame.display.update()
    clock.tick(10)