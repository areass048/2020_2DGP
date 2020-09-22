import random
from pico2d import *

RES_DIR = '../../resource'

class Grass:
	def __init__(self):
		self.image = load_image(RES_DIR + '/grass.png')
	def draw(self):
		self.image.draw(400, 30)
	def update(self):
		pass

class Ball:
	def __init__(self):
		self.image = load_image(RES_DIR + '/ball21x21.png')
	def draw(self):
		self.image.draw(400, 30)
	def update(self):
		pass

class Boy:
	#constructor
	# def __init__(self, pos, delta):
	# 	self.x, self.y = pos
	# 	self.dx, self.dy = delta
	def __init__(self):
		self.x = 400
		self.y = 300
		self.dx, self.dy = 0, 0
		self.fidx = random.randint(0, 7)
		self.image = load_image(RES_DIR + '/animation_sheet.png')
		self.action = 3
	def draw(self):
		self.image.clip_draw(self.fidx * 100, self.action * 100, 100, 100, self.x, self.y)
	def update(self):

		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx + 1) % 8
	def handle_event(self, e):
		prev_dx = self.dx
		if e.type == SDL_KEYDOWN:
			if e.key == SDLK_LEFT:
				self.dx -= 2
			elif e.key == SDLK_RIGHT:
				self.dx += 2
			elif e.key == SDLK_UP:
				self.dy += 2
			elif e.key == SDLK_DOWN:
				self.dy -= 2

		elif e.type == SDL_KEYUP:
			if e.key == SDLK_LEFT:
				self.dx += 2
			elif e.key == SDLK_RIGHT:
				self.dx -= 2
			elif e.key == SDLK_UP:
				self.dy -= 2
			elif e.key == SDLK_DOWN:
				self.dy += 2

		if prev_dx != self.dx:
			if self.dx < 0:
				self.action = 0
			elif self.dx > 0:
				self.action = 1
			elif prev_dx < 0:
				self.action = 2
			elif prev_dx > 0:
				self.action = 3

if __name__ == "__main__":
	print("Running test code ^_^")
