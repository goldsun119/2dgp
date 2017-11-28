import random
from pico2d import *

class Grass:
    def __init__(self):
        self.x, self.y = 400,100
        self.image = load_image('resource\\image\\under2.png')

    def draw(self):
        self.image.draw(self.x,self.y)


class Back:
    def __init__(self):
        self.x,self.y = 400,250
        self.image = load_image('resource\\image\\back.jpg')

    def draw(self):
        self.image.draw(400, 250)