from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x,y)
    delay(0.1)
    
def run_ciecle():
    print('CIRCLE')
    
    r, cx, cy = 300, 800//2, 600//2
    
    for degree in range(0,360,3):
        theta = math.radians(degree) 
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
    
        draw_boy(x,y)

    pass


def run_top():
    print('TOP')
    for x in range(0,800,10):
        draw_boy(x,550)
    pass

def run_right():
    print('right')
    for y in range(550, 0 , -10):
        draw_boy(790,y)
    pass

def run_bottom():
    print('bottom')
    for x in range(790, 0, -10):
        draw_boy(x,40)
    pass

def run_left():
    print('left')
    for y in range(10,550,10):
        draw_boy(10, y)
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left() 
    pass

def run_lefttop():
    y = 10
    for x in range(10,370, 10):
        y += 10
        draw_boy(x,y)
    pass

def run_rightbottom():
    y = 370
    for x in range(370,700,10):
        y -= 10
        draw_boy(x,y)
    pass
    
def run_triangle():
    print('triangle')
    run_bottom()
    run_lefttop()
    run_rightbottom()
    
while True:
    run_ciecle() 
    run_rectangle()
    run_triangle()
    
    
close_canvas()
