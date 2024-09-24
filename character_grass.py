from pico2d import *

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def run_ciecle():
    print('CIRCLE')
    pass #내용이 전혀 없는 빈 함수다.

def run_rectangle():
    print('RECTANGLE')
    pass    

while True:
    run_ciecle() #함수로 뼈대를 잡는게 중요하다
    run_rectangle()

close_canvas()
