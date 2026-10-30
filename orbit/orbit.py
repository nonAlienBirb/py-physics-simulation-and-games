
import pygame, sys, time
from pygame.math import Vector2
from scipy import constants

pygame.init()

G = constants.G

def CalculateGravitationalForce(m1, m2, r):
    return G*m1*m2/r**2
def CalculateGravitationalAcceleration(m2, r):
    return G*m2/r**2
def _():
    pass

# print(CalculateGravitationalForce(5.972*(10**24), 7.348*(10**22), 3.844*(10**8)))
ScreenSize = 600

Screen = pygame.display.set_mode((800, ScreenSize))
pygame.display.set_caption('Orbit test')
clock = pygame.time.Clock()

class Planet:
    def __init__(self, radius = 10 , mass = 1, velocity = Vector2(5,0) , acceleration = Vector2(-1, 0), position = Vector2(ScreenSize/2,ScreenSize/2)):
        self.Radius = radius
        self.Mass = mass
        self.Velocity = velocity
        self.Position = position
        self.Acceleration = acceleration
        self.counter = 0
        self.c = False
    def draw(self):
        self.Position = self.Position + self.Velocity + (self.Acceleration*self.counter)
        pygame.draw.circle(Screen,(100,100,100),self.Position,self.Radius)
        if self.c == True:
            self.counter += 1
            self.c = False
        print(f"c = {self.counter}")
        if (self.Position - Vector2(ScreenSize/2 ,ScreenSize/2 )).magnitude() < 2:
            self.Acceleration *= -1
            self.counter = 0

    def move(self):
        self.Position = self.Position + self.Velocity


p = Planet()

start = time.perf_counter()

while True:
    now = time.perf_counter()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    Screen.fill((0,0,0))
    p.draw()
    pygame.display.update()
    clock.tick(60)
    elapsed = now - start
    target_time  = (p.counter + 1 )*0.25
    if abs(elapsed - target_time) <= 0.01:
        p.c = True
