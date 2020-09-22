from pico2d import *
import random

open_canvas()


class Boy:
    def __int__(self):
        self.image = load_image("../resource/animation_sheet.png")
        self.x, self.y = random.randint(0, 300), 85
        self.frame_index = 0
        self.dx = 2
        self.action = 0

    def draw(self):
        self.image.clip_draw(100 * self.frame_index, 100 * self.action, 100, 100, self.x, 85)

    def update(self):
        self.x += self.dx
        if self.x % 100 == 0:
            self.action = (self.action + 1) % 4
        self.frame_index = (self.frame_index + 1) % 8


class Grass:
    def draw(self):
        self.image.draw(400, 30)


grass = Grass()

team = [Boy() for i in range(11)]
# boy.hello = 'world'
# type name = UpperCamelCase
# method name = lowerCamelCase

grass.image = load_image('../resource/grass.png')

running = True

while running:

    clear_canvas()
    grass.draw()
    for b in team:
        b.draw()
    update_canvas()

    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

    for b in team:
        b.update()

    if team[0].x > get_canvas_width():
        running = False

    delay(0.04)

close_canvas()