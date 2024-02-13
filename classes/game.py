import base64
import time
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Game:
    """
    Arcade Space Invaders game class.

    Keys:
        [x] start game
        [z] shoot
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
        self.__driver.execute_script('let event = new KeyboardEvent("keydown", { keyCode: 88 });document.dispatchEvent(event);')

    def fire(self):
        self.__driver.execute_script('let event = new KeyboardEvent("keydown", { keyCode: 90 });document.dispatchEvent(event);')

    def left(self):
        self.__driver.execute_script('let event = new KeyboardEvent("keydown", { keyCode: 37 });document.dispatchEvent(event);')
    
    def right(self):
        self.__driver.execute_script('let event = new KeyboardEvent("keydown", { keyCode: 39 });document.dispatchEvent(event);')

    def quit(self):
        self.__driver.quit()

    def get_image_png(self):
        # get the canvas as a PNG base64 string
        canvas_base64 = self.__driver.execute_script(
            "return arguments[0].toDataURL('image/png').substring(21);",
            self.__canvas)
        # decode from base64 to byte object
        img_bytes = base64.b64decode(str(canvas_base64))
        # Convert to img object
        return Image.open(BytesIO(img_bytes), 'r')

    def get_image_bw(self):
        # get screen as png and convert to black & white image
        img_png = self.get_image_png()
        return img_png.convert("1", dither=0)
