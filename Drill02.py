from pico2d import *
import math

open_canvas()

character = load_image('character.png')
grass = load_image('grass.png')

def rander_frame(x, y):
		clear_canvas_now()
		grass.draw_now(400, 30)
		character.draw_now(x, y)
		delay(0.1)

rander_frame(400, 90)

def run_circle():
	cx, cy, r = 400, 300, 200
	for deg in range(0, 360, 5):
		x = cx + r * math.cos(math.radians(deg))
		y = cy + r * math.sin(math.radians(deg))
		rander_frame(x, y)


def run_rectangle():
	#bottom line
	#for x in range(50, 750 + 1, 5):
	#	rander_frame(x, 90)

	#right line
#	for y in range(90, 550 + 1, 5):
#		rander_frame(750, y)

	#top line
#	for x in range(750, 50 - 1, -5):
#		rander_frame(x, 550)

	#left line
	for y in range(550, 90 - 1, -5):
		rander_frame(50, y)




while True:
	#run_circle()
	run_rectangle()
	break


close_canvas()