import random
from pico2d import *

class Grass:

    def __init__(self):
        self.x, self.y = 400,90
        self.image = load_image('resource\\image\\under2.png')
        self.bgm = load_music('resource\\sound\\bgm.mp3')

        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x,self.y)


class Back:
    def __init__(self):
        self.x,self.y = 400,250
        self.image = load_image('resource\\image\\back.jpg')

    def draw(self):
        self.image.draw(400, 250)