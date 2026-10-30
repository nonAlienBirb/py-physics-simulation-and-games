import pygame,sys,time
from pygame import Vector2

pygame.init()

ScreenWidth, ScreenHeight = 800, 600

WIN = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("FallinfTest")

clock = pygame.time.Clock()

class Object :
    def __init__(self, mass:float = 10, radius:float = 25, color:tuple = (200,200,200), speed:Vector2 =Vector2(6, 0), position:Vector2 = Vector2(ScreenWidth//2,ScreenHeight//2)):
        self.Mass = mass
        self.Radius = radius
        self.Color = color
        self.Speed = speed
        self.Position = position
        self.gravity = Vector2(0, 0.5)
        self.stuff = []
        
    def update(self):

        if self.Position.y + self.Radius >= ScreenHeight:
                self.Position.y= ScreenHeight - self.Radius
        elif self.Position.y - self.Radius <= 0:
                self.Position.y = self.Radius

        pygame.draw.circle(WIN,self.Color,(int(self.Position.x),int(self.Position.y)),self.Radius)
        
        if self.Position.y + self.Radius >= ScreenHeight or self.Position.y - self.Radius <= 0:
            self.Speed.y *= -0.8
            self.Speed.x *= 0.9
            
        if self.Position.x + self.Radius >= ScreenWidth or self.Position.x - self.Radius <= 0:
            self.Speed.x *= -0.8
            
        self.Speed += self.gravity
        self.Position += self.Speed

        print(f"speed: {self.Speed}, pos: {self.Position}, g: {self.gravity}")

bodyList =[Object(),
           Object(),
           Object()]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    WIN.fill((0,0,0))

    ball.update()

    pygame.display.update()
    clock.tick(60)