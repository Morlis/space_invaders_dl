import configparser
import os

class Config:
    config = configparser.ConfigParser()

    def __init__(self):
        self.__readConfig()

    @property
    def chromeDriver(self):
        return self.__chromeDriver
    
    @chromeDriver.setter
    def chromeDriver(self, var):
        self.__chromeDriver = var

    @property
    def gameUrl(self):
        return self.config['game']['url']

    # Read config values
    def __readConfig(self):
        self.config.read('config/config.ini')
        self.chromeDriver = os.path.join(os.getcwd(), self.config.get(
            section='DEFAULT', 
            option='chromeDriver',  
            fallback='chromedriver/win32/chromedriver.exe'))
