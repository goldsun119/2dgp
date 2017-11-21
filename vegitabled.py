import random

from pico2d import *


class Vk:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 18.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 10, 280
        Vk.image = load_image('resource\\image\\vk.png')

    def update(self, frame_time):
        distance = Vk.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 150, self. x + 45, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Bro:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 18.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 200, 100
        Bro.image = load_image('resource\\image\\bro.png')

    def update(self, frame_time):
        distance = Bro.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 150, self. x + 45, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Gaji:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 10, 280
        Gaji.image = load_image('resource\\image\\gaji.png')

    def update(self, frame_time):
        distance = Gaji.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 150, self. x + 45, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Dico:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 20.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 200, 100
        Dico.image = load_image('resource\\image\\dico.png')

    def update(self, frame_time):
        distance = Dico.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 150, self. x + 45, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Carrot:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 22.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 10, 280
        Carrot.image = load_image('resource\\image\\carrot.png')

    def update(self, frame_time):
        distance = Carrot.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 150, self. x + 45, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Ca:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 22.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        self.x, self.y = 200, 100
        Ca.image = load_image('resource\\image\\ca.png')

    def update(self, frame_time):
        distance = Ca.RUN_SPEED_PPS * frame_time
        self.x -= distance

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 15, self.y - 150, self. x + 45, self.y + 100

    def draw_bb(self):
        draw_rectangle(*self.get_bb())