from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Game:
    """
    Arcade Space Invaders properties class.

    Keys:   
        [5] insert coin
        [1] player1 select
        [control] shoot
        [right][reft] move
    """
    num_actions = 3

    def __init__(self, driver, canvas):
        self.__driver = driver
        self.__canvas = canvas
        self.__wrapper = driver.find_element(By.ID, 'wrap')

    def insertCoin(self):
        self.__wrapper.send_keys('5')

    def playerOne(self):
        self.__wrapper.send_keys('1')

    def fire(self):
        self.__wrapper.send_keys(Keys.CONTROL)
