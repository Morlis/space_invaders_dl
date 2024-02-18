import base64
import numpy as np
import cv2
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

    def get_canvas_bytes(self):
        # get the canvas as a PNG base64 string
        canvas_base64 = self.__driver.execute_script(
            "return arguments[0].toDataURL('image/png').substring(21);",
            self.__canvas)
        # decode from base64 to byte object
        img_bytes = base64.b64decode(str(canvas_base64))
        # Convert to img object
    
        return img_bytes

    def get_image_png(self):
        # Convert to PIL Image object
        return Image.open(BytesIO(self.get_canvas_bytes()), 'r')

    def get_image_bw_png(self):
        # get screen as png and convert to black & white image
        return self.get_image_png().convert("1", dither=0)

    def get_image(self):
        # Convert string buffer to numpy array
        nparr = np.frombuffer(self.get_canvas_bytes(), np.uint8)
        # Create cv2 image from byte np array
        return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    def get_image_gray(self):
        # Create cv2 image from byte np array
        return cv2.cvtColor(self.get_image(), cv2.COLOR_BGR2GRAY)
    
    def get_image_bw(self):
        # Convert image to black & white
        return cv2.threshold(self.get_image_gray(), 127, 255, cv2.THRESH_BINARY)[1]

    
