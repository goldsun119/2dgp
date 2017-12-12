from pico2d import*

import stage_state
import boy

#버튼 추가
class UI:
    def __init__(self):
        self.number0_image = load_image('resource\\Image\\Number\\0.png')
        self.number1_image = load_image('resource\\Image\\Number\\1.png')
        self.number2_image = load_image('resource\\Image\\Number\\2.png')
        self.number3_image = load_image('resource\\Image\\Number\\3.png')
        self.number4_image = load_image('resource\\Image\\Number\\4.png')
        self.number5_image = load_image('resource\\Image\\Number\\5.png')
        self.number6_image = load_image('resource\\Image\\Number\\6.png')
        self.number7_image = load_image('resource\\Image\\Number\\7.png')
        self.number8_image = load_image('resource\\Image\\Number\\8.png')
        self.number9_image = load_image('resource\\Image\\Number\\9.png')

        self.hp_image = load_image('resource\\Image\\hp2.png')

        self.playerscore = stage_state.boy.meatcount
        self.playerhp = stage_state.boy.lifecount

    def __del__(self):
        self.exit()


    def enter(self):
        pass


    def update(self, _events):
        self.playerhp = stage_state.boy.lifecount

        pass


    def draw(self):
            # 점수가져오기
            self.playerscore = (int)(stage_state.boy.meatcount)

            #젤리카운트 draw
            self.score_draw((int)(self.playerscore / 100), 650, 550)
            self.score_draw((int)(self.playerscore % 100 / 10), 700, 550)
            self.score_draw((int)(self.playerscore % 10), 750, 550)

            self.hp_image.clip_draw(0,0, self.playerhp,13,340-(500-self.playerhp)/2,30)

    def exit(self):
        del (self.number0_image)
        del (self.number1_image)
        del (self.number2_image)
        del (self.number3_image)
        del (self.number4_image)
        del (self.number5_image)
        del (self.number6_image)
        del (self.number7_image)
        del (self.number8_image)
        del (self.number9_image)



    def score_draw(self, number, x, y):
        if number == 0:
            self.number0_image.draw(x, y)
        elif number == 1:
            self.number1_image.draw(x, y)
        elif number == 2:
            self.number2_image.draw(x, y)
        elif number == 3:
            self.number3_image.draw(x, y)
        elif number == 4:
            self.number4_image.draw(x, y)
        elif number == 5:
            self.number5_image.draw(x, y)
        elif number == 6:
            self.number6_image.draw(x, y)
        elif number == 7:
            self.number7_image.draw(x, y)
        elif number == 8:
            self.number8_image.draw(x, y)
        elif number == 9:
            self.number9_image.draw(x, y)