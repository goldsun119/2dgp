import random
from pico2d import *

class Grass:
    image = None
    bgm = None

    def __init__(self):
        self.x, self.y = 400,90
        if Grass.image == None:
            Grass.image = load_image('resource\\image\\under2.png')

        if Grass.image == None:
            Grass.bgm = load_music('resource\\sound\\bgm.mp3')
            Grass.bgm.set_volume(64)
            Grass.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x,self.y)


class Back:
    image = None
    def __init__(self):
        self.x,self.y = 400,250
        if Back.image == None:
            Back.image = load_image('resource\\image\\back.jpg')

    def draw(self):
        self.image.draw(400, 250)