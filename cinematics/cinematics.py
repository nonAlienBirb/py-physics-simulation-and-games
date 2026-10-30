from raylib import *
from pyray import *

win_width = 700
win_height = 500

init_window(win_width, win_height,"text")

class Particle:
    def __init__(self, pos):
        self.size = 20
        self.pos = pos
        self.direction = Vector2()
        self.acceleration = Vector2()
        self.speed = Vector2()
        self.outputForce = Vector2(600, 600)
        self.center = Vector2(self.pos.x , self.pos.y
                              )
    
    def input(self):
        self.direction.x = int(is_key_down(KEY_RIGHT)) - int(is_key_down(KEY_LEFT))
        self.direction.y = int(is_key_down(KEY_DOWN)) - int(is_key_down(KEY_UP))
    
    def boundary_control(self):            
        if not self.size <= self.pos.x <= win_width - self.size:
            self.speed.x = 0

        if not self.size <= self.pos.y <= win_height - self.size:
            self.speed.y = 0

        self.pos.x = max(self.size, min(self.pos.x, win_width - self.size))
        self.pos.y = max(self.size, min(self.pos.y, win_height - self.size))
    
    def gravity(self, externals):
        
        if externals.x < self.pos.x:
            self.direction.x = -1
        elif externals.x > self.pos.x:
            self.direction.x = 1
        else:
            self.direction.x = 0

        if externals.y < self.pos.y:
            self.direction.y = -1
        elif externals.y > self.pos.y:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
    def update(self, dt):
        g_pos = Vector2(win_width/2, win_height/2)
        self.gravity(g_pos)
        g = 400
        self.acceleration.x = self.direction.x * g
        self.acceleration.y = self.direction.y * g

        self.speed.x += self.acceleration.x * dt
        self.speed.y += self.acceleration.y * dt

        self.pos.x += self.speed.x * dt
        self.pos.y += self.speed.y * dt

        self.boundary_control()

    def draw(self):
        draw_circle_v(self.pos, self.size, RED)
        draw_circle_v(Vector2(win_width/2, win_height/2), 10, WHITE)


p1 = Particle(Vector2(200,200))

while not window_should_close():
    dt = GetFrameTime()

    p1.update(dt)

    begin_drawing()
    clear_background(BLACK)
    p1.draw()
    end_drawing()
close_window()