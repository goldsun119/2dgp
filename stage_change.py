from pico2d import *
import stage2_state
import stage3_state
import stage_state
import game_framework


class Stage:
    PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
    RUN_SPEED_KMPH = 18.0  # Km/Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.x,self.y = 400,200
        self.stage2_image = load_image('resource\\image\\stage2.png')
        self.stage3_image = load_image('resource\\image\\stage2.png')
        self.count = 2

    def draw(self):
        if self.count == 2:
            self.stage2_image.draw(self.x, self.y)
        if self.count == 3:
            self.stage2_image.draw(self.x, self.y)

    def update(self, frame_time):
        global logo_time
        if (logo_time > 1.0):
            logo_time = 0
            self.count+=1
            game_framework.push_state(stage2_state)

        distance = Stage.RUN_SPEED_PPS * frame_time
        self.x -= distance

        delay(0.01)
        logo_time += 0.01

    def enter():
