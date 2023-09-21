from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

grass.draw_now(400, 30)
character.draw_now(400, 90)
delay(1)

close_canvas()