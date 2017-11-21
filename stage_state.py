from pico2d import *
import json
import game_framework
import random
import collision


from boy import Boy # import Boy class from boy.py
from meat import Meat
from grass import Grass,Back
from vegitabled import Vk,Bro,Gaji,Dico,Carrot,Ca

boy = None
meats = None
grass = None
vks = None
back = None
bros = None
gajis= None
dicos=None
carrots = None
Cas = None

st1 = True
st2 = False
st3 = False

MAP_SIZE=10000      #cm = 100m 달리기

meat_count = 0


def create_world():

    UP_X = [700, 800, 1300, 1400, 1800, 2300, 2400, 2900, 3000, 3600, \
            3700, 4200, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1100, 2000, 3300, 4600, 6700, 8600, 9600]

    global boy, grass, meats, vks, back, bros, gajis, dicos, cas, carrots
    boy = Boy()
    back = Back()
    grass = Grass()
    meats = [Meat() for i in range(190)]
    vks = [Vk() for i in range(32)]
    bros = [Bro() for i in range(7)]
    for i in range(190):
        meats[i].x=(50*i)+400
        if not meats[i].x in UP_X:
            for j in range(31):
                print(UP_X[j+1]-UP_X[j])
                if (meats[i].x>=UP_X[j]) and (meats[i].x<=UP_X[j+1]):
                    if not (UP_X[j+1]-UP_X[j]==100):
                        meats[i].y = 150
        if meats[i].x in DOWN_X:
            meats[i].y=200

        meats[i].x+=10
    for i in range(32):
        vks[i].x=UP_X[i]
    for i in range(7):
        bros[i].x = DOWN_X[i]


def create_world2():
    UP_X = [800, 900, 1300, 1400, 1800, 2300, 2400, 2700, 3000, 3600, \
            3700, 4100, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1100, 1600, 2000, 3250, 3300, 4600, 5200, 6300, 6700, 8600, 9600]

    global boy, grass, meats, vks, back, bros, gajis, dicos, cas, carrots
    boy = Boy()
    back = Back()
    meats = [Meat() for i in range(190)]
    grass = Grass()

    vks = [Vk() for i in range(32)]
    bros = [Bro() for i in range(7)]

    gajis = [Gaji() for i in range(32)]
    dicos = [Dico() for i in range(11)]

    cas = [Gaji() for i in range(32)]
    carrots = [Dico() for i in range(11)]

    for i in range(190):
        meats[i].x = (50 * i) + 400
        if not meats[i].x in UP_X:
            for j in range(31):
                if (meats[i].x >= UP_X[j]) and (meats[i].x <= UP_X[j + 1]):
                    if not (UP_X[j + 1] - UP_X[j] == 100):
                        meats[i].y = 150
        else:
            meats[i - 1].y = -400

        if meats[i].x in DOWN_X:
            meats[i].y = 200

        meats[i].x += 10
    for i in range(32):
        gajis[i].x = UP_X[i]
    for i in range(11):
        dicos[i].x = DOWN_X[i]



def create_world3():
    UP_X = [800, 900, 1300, 1400, 1800, 2300, 2400, 2700, 3000, 3600, \
            3700, 4100, 4300, 4400, 4900, 5000, 5500, 5600, 6100, 6500, \
            7000, 7100, 7200, 7300, 7800, 7900, 8200, 8300, 8800, 8900, \
            9400, 9900]

    DOWN_X = [1050, 1600, 2000, 3250, 3300, 4600, 4650, 5200, 5250, 6300, 6700, 6750, 8600, 9600, 9700]

    global boy, grass, meats, vks, back, bros, gajis, dicos, cas, carrots
    boy = Boy()
    back = Back()
    meats = [Meat() for i in range(190)]
    grass = Grass()

    vks = [Vk() for i in range(32)]
    bros = [Bro() for i in range(7)]

    gajis = [Gaji() for i in range(32)]
    dicos = [Dico() for i in range(11)]

    carrots = [Carrot() for i in range(32)]
    cas = [Ca() for i in range(15)]

    for i in range(190):
        meats[i].x = (50 * i) + 400
        if not meats[i].x in UP_X:
            for j in range(31):
                if (meats[i].x >= UP_X[j]) and (meats[i].x <= UP_X[j + 1]):
                    if not (UP_X[j + 1] - UP_X[j] == 100):
                        meats[i].y = 150
        else:
            meats[i - 1].y = -400

        if meats[i].x in DOWN_X:
            meats[i].y = 200

        meats[i].x += 10
    for i in range(32):
        carrots[i].x = UP_X[i]
    for i in range(15):
        cas[i].x = DOWN_X[i]


def change_world():
    global back




def destroy_world():
    global boy, grass, meats, vks, bros

    del(meats)
    del(vks)
    del(bros)


def enter():
    open_canvas(800,400,sync=True)
    game_framework.reset_time()
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
    global meat_count

    boy.update(frame_time)

    for meat in meats:
        meat.update(frame_time)

    for vk in vks:
        vk.update(frame_time)

    for bro in bros:
        bro.update(frame_time)

    for meat in meats:
        if collision.collide(boy,meat):
            meats.remove(meat)
            meat_count+=1

#    for gaji in gajis:
#        gaji.update(frame_time)

#    for dico in dicos:
#        dico.update(frame_time)

#    for carrot in carrots:
#        carrot.update(frame_time)

#    for ca in cas:
#        ca.update(frame_time)



def draw(frame_time):
    clear_canvas()
    back.draw()
    grass.draw()
    boy.draw()

    for meat in meats:
        meat.draw()

    for vk in vks:
        vk.draw()

    for bro in bros:
        bro.draw()

#    for gaji in gajis:
 #       gaji.draw()

#    for dico in dicos:
#       dico.draw()

#    for carrot in carrots:
 #       carrot.draw()

#    for ca in cas:
 #       ca.draw()

    boy.draw_bb()

    update_canvas()






