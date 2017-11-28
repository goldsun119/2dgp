from pico2d import *
import json
import game_framework
import random
import collision
import stage2_state


from boy import Boy # import Boy class from boy.py
from meat import Meat22
from grass import Grass,Back
from vegitabled import Carrot,Ca

boy = None
meats = None
grass = None
back = None

carrots = None
Cas = None

MAP_SIZE=10000      #cm = 100m 달리기


def create_world():
    UP_X = [800, 900, 1300, 1400, 1800, 2300, 2400, 2700, 3000, 3600, \
            3700, 4100, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1050, 1600, 2000, 3250, 3300, 4600, 4650, 5200, 5250, 6300, 6700, 6750, 8600, 9600, 9700]

    global boy, grass, meats, back, cas, carrots
    boy = stage2_state.boy
    back = Back()
    meats = [Meat22() for i in range(190)]
    grass = Grass()

    carrots = [Carrot() for i in range(32)]
    cas = [Ca() for i in range(15)]

    for i in range(190):
        meats[i].x = (50 * i) + 400
        if not meats[i].x in UP_X:
            for j in range(31):
                if (meats[i].x >= UP_X[j]) and (meats[i].x <= UP_X[j + 1]):
                    if not (UP_X[j + 1] - UP_X[j] == 100):
                        meats[i].y = 250
        else:
            meats[i - 1].y = -400

        if meats[i].x in DOWN_X:
            meats[i].y = 300

        meats[i].x += 10
    for i in range(32):
        carrots[i].x = UP_X[i]
    for i in range(15):
        cas[i].x = DOWN_X[i]


def destroy_world():
    global boy, grass, back, meats, carrots, cas

    del(boy)
    del(grass)
    del(back)
    del(meats)
    del(carrots)
    del(cas)


def enter():
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                boy.handle_event(event)

def update(frame_time):
    global boy

    boy.update(frame_time)

    for meat in meats:
        meat.update(frame_time)

    for meat in meats:
        if collision.collide(boy,meat):
            meats.remove(meat)
            boy.meatcount+=1
            print(boy.meatcount)
    for carrot in carrots:
        carrot.update(frame_time)

    for ca in cas:
        ca.update(frame_time)

    for carrot in carrots:
            if collision.collide(boy,carrot):
                if not carrot == carrots[-1]:
                    carrots.remove(carrot)


    for ca in cas:
            if collision.collide(boy,ca):
                cas.remove(ca)

#    if carrots[-1].x <= 10 :
 #       game_framework.push_state(end_state)


def draw(frame_time):
    clear_canvas()
    back.draw()
    grass.draw()
    boy.draw()

    for meat in meats:
        meat.draw()

    for carrot in carrots:
        carrot.draw()
        carrot.draw_bb()

    for ca in cas:
        ca.draw()
        ca.draw_bb()

    boy.draw_bb()

    update_canvas()