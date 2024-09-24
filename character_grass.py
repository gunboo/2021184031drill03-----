from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_ciecle():
    print('CIRCLE')

    clear_canvas_now()
    boy.draw_now(400.300)
    delay(0.1)

def run_rectangle():
    print('RECTANGLE')
    pass    

while True:
    run_ciecle() 
    run_rectangle()
    break

close_canvas()
