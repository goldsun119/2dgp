import random
import game_framework
import start_state

from pico2d import *

class Boy:
    PIXEL_PER_METER = (10.0 / 0.1)           # 10 pixel 10 cm
    RUN_SPEED_KMPH = 1.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None
    vegitable_eat_sound = None
    item_eat_sound = None
    jump_sound = None


    RIGHT_JUMP, RIGHT_RUN, SLIDE, COLLID, DIE = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 100, 190
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.jumpCount = 0
        self.isJump = False
        self.isDead = False
        self.isCollid = False
        self.state = self.RIGHT_RUN
        self.meatcount = 0
        self.lifecount = 500
        self.dead_frame = 0
        Boy.run_image = load_image('resource\\image\\run2.png')
        Boy.dead_image = load_image('resource\\image\\dead.png')
        Boy.collid_image = load_image('resource\\image\\collid2.png')
        Boy.slide_image = load_image('resource\\image\\slide2.png')
        Boy.jump_image = load_image('resource\\image\\jump22.png')
        Boy.jump2_image = load_image('resource\\image\\jump222.png')
        if Boy.vegitable_eat_sound == None:
            Boy.vegitable_eat_sound = load_wav('resource\\sound\\bomit.wav')
            Boy.vegitable_eat_sound.set_volume(32)
        if Boy.item_eat_sound == None:
            Boy.item_eat_sound = load_wav('resource\\sound\\swallow.wav')
            Boy.item_eat_sound.set_volume(100)
        if Boy.jump_sound == None:
            Boy.jump_sound = load_wav('resource\\sound\\jump.wav')
            Boy.jump_sound.set_volume(100)


    def eat_vegitable(self, vegitable):
        self.vegitable_eat_sound.play()
        self.lifecount-=10
        pass

    def eat_item(self, item):
        self.item_eat_sound.play()
        pass

    def jump_play(self):
        self.jump_sound.play()
        pass

    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 3

        # 죽는지 확인
        if self.lifecount> 0 :
            self.lifecount -= 1
            self.lifecount = min(self.lifecount,500)

        if self.lifecount<=0:
            self.state=self.DIE
            self.isDead=True

        if self.isDead:
            self.dead_frame+=1
            if self.dead_frame>3:
                self.dead_frame=3


        if self.isJump:
            self.jumpCount += 1
            if self.jumpCount == 30:
                self.jumpCount = 0
                self.isJump = False
            elif self.jumpCount < 15:
                self.y += (15 - self.jumpCount) * 2
            else:
                self.y -= (self.jumpCount - 15) * 2

        if self.isCollid:
            current_time = get_time()
            if current_time >= 3.0:
                self.isCollid = False



    def draw(self):
        if self.RIGHT_RUN and self.isJump == False and self.state == self.RIGHT_RUN and self.isCollid == False:
            self.run_image.clip_draw(self.frame * 100, 0, 100, 130, self.x, self.y+20)
        elif self.isCollid:
            self.collid_image.draw(self.x+20,self.y)
        elif self.state == self.SLIDE:
            self.slide_image.draw(self.x,self.y-20)
        elif (self.isJump) and (self.jumpCount < 12):
            self.jump_image.draw(self.x,self.y)
        elif self.isJump:
            self.jump2_image.draw(self.x,self.y)
        elif self.isDead:
            self.dead_image.clip_draw(self.dead_frame * 100 , 0 ,100,100,self.x,self.y)



    def get_bb(self):
        if self.isJump:
            return self.x - 30, self.y - 60, self.x + 40, self.y + 50
        if self.isCollid:
            return self.x - 75, self.y - 50, self.x , self.y + 80
        if self.state == self.SLIDE:
            return self.x - 50, self.y - 50, self.x + 60, self.y + 15
        if self.isDead:
            return self.x-50, self.y-50, self.x+40, self.y+20
        return self.x - 30, self.y - 35, self.x + 40, self.y + 80


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.isDead:
                game_framework.change_state(start_state)
            else:
                self.jump_play()
                self.state = self.RIGHT_JUMP
                self.isJump=True
                self.dir = -1
        if (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
                self.state = self.RIGHT_RUN
                self.dir = -1
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                self.state = self.SLIDE
                self.dir = -1
        if (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
                self.state = self.RIGHT_RUN
                self.dir = -1