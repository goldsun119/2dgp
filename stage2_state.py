from pico2d import *
import json
import game_framework
import random
import collision
import stage3_state
import stage_state


from boy import Boy # import Boy class from boy.py
from meat import Meat20, meat_count
from grass import Grass,Back
from vegitabled import Gaji,Dico

boy = None
meats = None
grass = None
back = None
gajis= None
dicos=None

#stage2_image = load_image('resource\\image\\stage2.png')

MAP_SIZE=10000      #cm = 100m 달리기


def create_world():
    UP_X = [800, 900, 1300, 1400, 1800, 2300, 2400, 2700, 3000, 3600, \
            3700, 4100, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1100, 1600, 2000, 3250, 3300, 4600, 5200, 6300, 6700, 8600, 9600]

    global boy, grass, meats, back, gajis, dicos
    boy = stage_state.boy
    back = Back()
    meats = [Meat20() for i in range(190)]
    grass = Grass()

    gajis = [Gaji() for i in range(32)]
    dicos = [Dico() for i in range(11)]

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
        gajis[i].x = UP_X[i]
    for i in range(11):
        dicos[i].x = DOWN_X[i]


def destroy_world():
    global boy, grass, back, meats, gajis, dicos

    del (boy)
    del (grass)
    del (back)
    del (meats)
    del (gajis)
    del (dicos)


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

    for gaji in gajis:
        gaji.update(frame_time)
        if gaji.x < -15:
            gajis.remove(gaji)

    for dico in dicos:
        dico.update(frame_time)
        if dico.x < -15:
            dicos.remove(dico)

    for gaji in gajis:
            if collision.collide(boy,gaji):
                if not gaji == gajis[-1]:
                    gajis.remove(gaji)

    for dico in dicos:
            if collision.collide(boy,dico):
                dicos.remove(dico)

    if gajis[-1].x <= -10 :
        game_framework.push_state(stage3_state)


def draw(frame_time):
    clear_canvas()
    back.draw()
    grass.draw()
    boy.draw()

    for meat in meats:
        meat.draw()

    for gaji in gajis:
        gaji.draw()
        gaji.draw_bb()

    for dico in dicos:
        dico.draw()
        dico.draw_bb()

    boy.draw_bb()

    update_canvas()