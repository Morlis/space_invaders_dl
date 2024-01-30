import base64
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


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
        self.__driver.execute_script(
            "arguments[0].getContext('webgl', {preserveDrawingBuffer: true});",
            canvas)
        self.__actions = ActionChains(driver)

    def insert_coin(self):
        self.__actions.send_keys('5')
        self.__actions.perform()

    def player_one(self):
        self.__actions.send_keys('1')
        self.__actions.perform()

    def start(self):
        self.insert_coin()
        time.sleep(0.5)
        self.player_one()

    def fire(self):
        self.__actions.send_keys(Keys.CONTROL)

    def get_image_png(self):
        # get the canvas as a PNG base64 string
        canvas_base64 = self.__driver.execute_script(
            "return arguments[0].toDataURL('image/png').substring(21);",
            self.__canvas)
        # decode and return
        return base64.b64decode(str(canvas_base64))
