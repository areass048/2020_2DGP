from pico2d import *

open_canvas()


class Boy:
    def __int__(self , x=0, y=85, dx=2):
        self.image = load_image('../resource/animation_sheet.png')
        self.x, boy.y = 0, 85
        self.frame_index = 0
        self.dx = 2
        self.action = 0

    def draw(self):
        self.image.clip_draw(100 * boy.frame_index, 100 * boy.action, 100, 100, boy.x, 85)

    def update(self):
        self.x += self.dx
        if self.x % 100 == 0:
            self.action = (self.action + 1) % 4
        boy.frame_index = (boy.frame_index + 1) % 8


class Grass:
    def __int__(self):
        self.image = load_image('../resource/grass.png')

    def draw(self):
        self.image.draw(400, 30)


gra = Grass()
boy = Boy()
# boy.hello = 'world'
# type name = UpperCamelCase
# method name = lowerCamelCase


b2 = Boy()
b2.x, b2.y, b2.dx = get_canvas_width(), 200, -2

running = True

while running:

    clear_canvas()
    gra.draw()
    boy.draw()
    update_canvas()

    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif(e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            running = False

    boy.update()

    if boy.x > get_canvas_width():
        running = False

    delay(0.04)

close_canvas()