from pico2d import *
import json
import game_framework
import random
import collision
import stage3_state
import stage_state
import ui
import item


from boy import Boy # import Boy class from boy.py
from meat import Meat20
from grass import Back
from vegitabled import Gaji,Dico

boy = None
boy_ui = None
meats = None
grass = None
back = None
gajis= None
dicos=None
cokes2 = None

#stage2_image = load_image('resource\\image\\stage2.png')

#MAP_SIZE=10000      #cm = 100m 달리기


def create_world():
    UP_X = [800, 900, 1300, 1400, 1800, 2300, 2400, 2700, 3000, 3600, \
            3700, 4100, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1100, 1600, 2000, 3250, 3300, 4600, 5200, 6300, 6700, 8600, 9600]

    COKE_X = [500, 1500, 2500, 3500, 4000, 4800, 6000, 6900, 7700, 9000, 9500]

    global boy, meats, back, gajis, dicos,cokes2,boy_ui
    boy = stage_state.boy
    boy_ui = ui.UI()
    back = Back()
    meats = [Meat20() for i in range(190)]

    gajis = [Gaji() for i in range(32)]
    dicos = [Dico() for i in range(11)]
    cokes2 = [item.Coke2() for i in range(11)]

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
        gajis[i].x = UP_X[i]
    for i in range(11):
        dicos[i].x = DOWN_X[i]
    for i in range(11):
        cokes2[i].x = COKE_X[i]
        cokes2[i].y = 250

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
    #destroy_world()
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
    boy_ui.update(frame_time)

    for coke in cokes2:
        if boy.lifecount <= 0:
            coke.distance = 0
        else:
            coke.update(frame_time)

    for coke in cokes2:
        if collision.collide(boy, coke):
            cokes2.remove(coke)
            boy.lifecount += 100
            boy.eat_item(coke)

    for meat in meats:
        if boy.lifecount <= 0:
            meat.distance = 0
        else:
            meat.update(frame_time)

    for meat in meats:
        if collision.collide(boy,meat):
            meats.remove(meat)
            boy.meatcount+=1

    for gaji in gajis:
        if boy.lifecount <= 0:
            gaji.distance = 0
        else:
            gaji.update(frame_time)
        if gaji.x < -20:
            gajis.remove(gaji)

    for dico in dicos:
        if boy.lifecount <= 0:
            dico.distance = 0
        else:
            dico.update(frame_time)
        if dico.x < -15:
            dicos.remove(dico)

    for gaji in gajis:
            if collision.collide(boy,gaji):
                if not gaji == gajis[-1]:
                    gajis.remove(gaji)
                boy.eat_vegitable(gaji)

    for dico in dicos:
            if collision.collide(boy,dico):
                dicos.remove(dico)
                boy.eat_vegitable(dico)

    if gajis[-1].x <= -10:
        game_framework.push_state(stage3_state)


def draw(frame_time):
    back.draw()
    stage_state.grass.draw()
    boy.draw()

    for coke in cokes2:
        coke.draw()

    for meat in meats:
        meat.draw()

    for gaji in gajis:
        gaji.draw()

    for dico in dicos:
        dico.draw()

    global boy_ui
    boy_ui.draw()

    update_canvas()