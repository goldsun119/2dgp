import random

from pico2d import *

class Grass:
    def __init__(self):
        self.x, self.y = 400,30
        self.image = load_image('resource\\image\\under.png')

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self,frame_time):
        self.life_time += frame_time
        self.total_frames += Grass.FRAMES_PER_ACTION * Grass.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10


class Back:
    def __init__(self):
        self.x,self.y = 400,200
        self.image = load_image('resource\\image\\back2.png')

    def draw(self):
        self.image.draw(400, 200)
