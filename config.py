import configparser
import os


class Config:
    configuration = configparser.ConfigParser()

    def __init__(self):
        self.__chrome_driver = None
        self.__read_config()

    @property
    def chrome_driver(self):
        return self.__chrome_driver

    @chrome_driver.setter
    def chrome_driver(self, var):
        self.__chrome_driver = var

    @property
    def game_url(self):
        return self.configuration['game']['url']

    # Read config values
    def __read_config(self):
        self.configuration.read('config/config.ini')
        self.chrome_driver = os.path.join(os.getcwd(), self.configuration.get(
            section='DEFAULT',
            option='chromeDriver',
            fallback='chromedriver/win32/chromedriver.exe'))
