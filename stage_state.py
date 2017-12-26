from pico2d import *
import json
import game_framework
import random
import collision
import stage2_state
import ui
import item


from boy import Boy # import Boy class from boy.py
from meat import Meat18, meat_count
from grass import Grass, Back
from vegitabled import Vk, Bro

boy = None
boy_ui = None
meats = None
grass = None
back = None
vks = None
bros = None
cokes = None
collid_time = 0.0


MAP_SIZE=10000      #cm = 100m 달리기


def create_world():

    UP_X = [700, 800, 1300, 1400, 1800, 2300, 2400, 2900, 3000, 3600, \
            3700, 4200, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1100, 2000, 3300, 4600, 6700, 8600, 9600]

    COKE_X = [1700, 2200, 2500, 3500, 4000, 4800, 6000, 6900, 7700, 9000]

    global boy, grass, meats, vks, back, bros, boy_ui, cokes
    boy = Boy()
    boy_ui = ui.UI()
    boy_ui.enter()
    back = Back()
    grass = Grass()
    cokes = [item.Coke() for i in range(10)]
    meats = [Meat18() for i in range(190)]
    vks = [Vk() for i in range(32)]
    bros = [Bro() for i in range(7)]

    for i in range(190):
        meats[i].x=(50*i)+400
        if not meats[i].x in UP_X:
            for j in range(31):
                if (meats[i].x >= UP_X[j]) and (meats[i].x <= UP_X[j+1]):
                    if not (UP_X[j+1]-UP_X[j] == 100):
                        meats[i].y = 250
        if meats[i].x in DOWN_X:
            meats[i].y = 300
        if meats[i].x in COKE_X:
            meats[i].y = 700

        meats[i].x += 10
    for i in range(32):
        vks[i].x=UP_X[i]
    for i in range(7):
        bros[i].x = DOWN_X[i]
    for i in range(10):
        cokes[i].x = COKE_X[i]
        cokes[i].y = 250

def destroy_world():
    global boy, grass, meats, vks, bros

    del(boy)
    del(grass)
    del(meats)
    del(vks)
    del(bros)


def enter():
    clear_canvas()
    game_framework.reset_time()
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
    global boy, collid_time
    boy.update(frame_time)

    boy_ui.update(frame_time)

    for meat in meats:
        if boy.lifecount <= 0:
            meat.distance = 0
        else:
            meat.update(frame_time)

    for coke in cokes:
        if boy.lifecount <= 0:
            coke.distance = 0
        else:
            coke.update(frame_time)

    for coke in cokes:
        if collision.collide(boy,coke):
            cokes.remove(coke)
            boy.lifecount+=100
            boy.eat_item(coke)

    for vk in vks:
        if boy.lifecount <= 0:
            vk.distance = 0
        else:
            vk.update(frame_time)
        if vk.x < -20:
            vks.remove(vk)


    for bro in bros:
        if boy.lifecount <= 0:
            bro.distance = 0
        else:
            bro.update(frame_time)
        if bro.x < -15:
            bros.remove(bro)


    for meat in meats:
        if collision.collide(boy,meat):
            meats.remove(meat)
            boy.meatcount+=1




    for vk in vks:
            if collision.collide(boy,vk):
                if not vk == vks[-1]:
                     vks.remove(vk)
                boy.eat_vegitable(vk)


    for bro in bros:
            if collision.collide(boy,bro):
                bros.remove(bro)
                boy.eat_vegitable(bro)

    if vks[-1].x <= -10 :
        game_framework.push_state(stage2_state)



def draw(frame_time):
    back.draw()
    grass.draw()
    boy.draw()

    for meat in meats:
        meat.draw()

    for vk in vks:
        vk.draw()

    for bro in bros:
        bro.draw()

    for coke in cokes:
        coke.draw()
    #ui draw
    global boy_ui
    boy_ui.draw()


    update_canvas()