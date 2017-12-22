import random

from pico2d import *


class Coke:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 17.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 10, 380
        Coke.image = load_image('resource\\image\\coke.png')

    def update(self, frame_time):
        distance = Coke.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 13, self.y - 18, self. x + 13, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Coke2:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 19.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 10, 380
        self.image = load_image('resource\\image\\coke.png')

    def update(self, frame_time):
        distance = Coke2.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 13, self.y - 18, self. x + 13, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Coke3:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 21.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 10, 380
        self.image = load_image('resource\\image\\coke.png')

    def update(self, frame_time):
        distance = Coke3.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 13, self.y - 18, self. x + 13, self.y + 18

    def draw_bb(self):
        draw_rectangle(*self.get_bb())