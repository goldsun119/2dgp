from pico2d import *
import json
import game_framework
import collision
import stage_state
import stage2_state
import ui
import item

from meat import Meat22
from grass import Back
from vegitabled import Carrot,Ca

boy = None
boy_ui = None
meats = None
grass = None
back = None
cokes3 = None

carrots = None
Cas = None

MAP_SIZE=10000      #cm = 100m 달리기


def create_world():
    UP_X = [800, 900, 1300, 1400, 1800, 2300, 2400, 2700, 3000, 3600, \
            3700, 4100, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1050, 1600, 2000, 3250, 3300, 4600, 4650, 5200, 5250, 6300, 6700, 6750, 8600, 9600, 9700]
    COKE_X = [500, 1700, 2200, 3500, 4000, 6000, 7700, 9000]

    global boy, meats, back, cas, carrots,cokes3,boy_ui
    boy = stage_state.boy
    back = Back()
    boy_ui = ui.UI()
    meats = [Meat22() for i in range(190)]

    cokes3 = [item.Coke3() for i in range(8)]

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
        if meats[i].x in COKE_X:
            meats[i].y = 700
        meats[i].x += 10
    for i in range(32):
        carrots[i].x = UP_X[i]
    for i in range(15):
        cas[i].x = DOWN_X[i]
    for i in range(8):
        cokes3[i].x = COKE_X[i]
        cokes3[i].y = 250

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
   # destroy_world()
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
    global boy, boy_ui

    boy.update(frame_time)
    boy_ui.update(frame_time)

    for coke in cokes3:
        if boy.lifecount <= 0:
            coke.distance = 0
        else:
            coke.update(frame_time)

    for coke in cokes3:
        if collision.collide(boy, coke):
            cokes3.remove(coke)
            boy.lifecount += 100
            boy.eat_item(coke)

    for meat in meats:
        if boy.lifecount <= 0:
            meat.distance = 0
        else:
            meat.update(frame_time)

    for meat in meats:
        if collision.collide(boy, meat):
            meats.remove(meat)
            boy.meatcount += 1


    for carrot in carrots:
        if boy.lifecount <= 0:
            carrot.distance = 0
        else:
            carrot.update(frame_time)
        if carrot.x < -30:
            carrots.remove(carrot)

    for ca in cas:
        if boy.lifecount <= 0:
            ca.distance = 0
        else:
            ca.update(frame_time)
        if ca.x < -30:
            cas.remove(ca)

    for carrot in carrots:
            if collision.collide(boy,carrot):
                if not carrot == carrots[-1]:
                    carrots.remove(carrot)
                boy.eat_vegitable(carrot)

    for ca in cas:
            if collision.collide(boy,ca):
                cas.remove(ca)
                boy.eat_vegitable(ca)

    if carrots[-1].x <= 0:
        boy_ui.clear = True

    #    if carrots[-1].x <= 10 :
 #       game_framework.push_state(end_state)


def draw(frame_time):
    back.draw()
    stage_state.grass.draw()
    boy.draw()

    for coke in cokes3:
        coke.draw()

    for meat in meats:
        meat.draw()

    for carrot in carrots:
        carrot.draw()

    for ca in cas:
        ca.draw()

    global boy_ui
    boy_ui.draw()


    update_canvas()