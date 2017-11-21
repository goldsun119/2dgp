import random

from pico2d import *


class Meat:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 18.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 0, 90
        if Meat.image == None:
            Meat.image = load_image('resource\\image\\meat50.png')

    def update(self, frame_time):
        distance = Meat.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 15, self. x + 20, self.y + 14

    def draw_bb(self):
        draw_rectangle(*self.get_bb())