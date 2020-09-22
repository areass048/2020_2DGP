import gfw
from pico2d import *
from gobj import *
import pause_state

def enter():
    global grass, boy
    grass = Grass()
    boy = Boy()

def update():
    boy.update()

def draw():
    grass.draw()
    boy.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_p:
            gfw.push(pause_state)
    boy.handle_event(e)


def exit():
    pass

def pause():
    pass
def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()
