import game_framework
import collision
from pico2d import *


name = "TitleState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('title.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(collision)
    pass


def draw():
    clear_canvas()
    image.draw(400,200)
    update_canvas()
    pass


def update():
    global logo_time
    if(logo_time > 1.0):
        logo_time = 0
        delay(0.01)
    logo_time += 0.01
    pass


def pause():
    pass


def resume():
    pass
