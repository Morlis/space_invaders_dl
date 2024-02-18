from classes.number_parser import Number_Parser

class Game_State:
    __DIGIT_SIZE = 9
    __LIVES_X = 21
    __LIVES_Y = 218
    __SCORE_Y = 42
    __SCORE_X = 37
    __STATE_X = 0
    __STATE_Y = 58
    __STATE_CX = 268
    __STATE_CY = 158

    shape = (158, 268)
    num_actions = 3
    number_parser = Number_Parser()

    def __init__(self, image=None):
        self.__image = image
        if self.__image is None:
            self.reset()
        else:
            self.__score = self.__calculate_score()
            self.__lives = self.__calculate_lives()      

    def __calculate_lives(self):
        if self.__image is None:
            return 0
        
        lives_digit = self.__image[self.__LIVES_Y:self.__LIVES_Y + self.__DIGIT_SIZE, 
                                   self.__LIVES_X:self.__LIVES_X + self.__DIGIT_SIZE]
        return self.number_parser.get_digit(lives_digit)

    def __calculate_score(self):
        if self.__image is None:
            return 0
        
        score_digits = [None] * 6

        for i in range(6):
            pos = 8 * i
            score_digits[i] = self.__image[self.__SCORE_Y:self.__SCORE_Y + self.__DIGIT_SIZE, 
                                           self.__SCORE_X + pos:self.__SCORE_X + pos + self.__DIGIT_SIZE]

        return self.number_parser.get_number(score_digits)
    
    def reset(self):
        self.__image = None
        self.__score = 0
        self.__lives = 3

    def state(self):
        if self.__image is None:
            return None
        
        return self.__image[self.__STATE_Y:self.__STATE_Y + self.__STATE_CY, 
                            self.__STATE_X:self.__STATE_X + self.__STATE_CX]
    
    def score(self):
        return self.__score
    
    def lives(self):
        return self.__lives

