import logging
from logging.config import fileConfig
import random
import configparser

fileConfig('../config/logging.ini')
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()
config.read('../config/setup.ini')

class sensor:
    def __init__(self):
        try:
            self.seed = config['sensor']['seed']
            random.seed(self.seed)
            logger.info('sensor class instantiated')
        except Exception as e:
            logger.exception(e)

    ### Method that will generate the data (random int numbers between 1 and 10)
    def generateData(self):
        try:
            return random.randint(1, 10)
        except Exception as e:
            logger.exception(e)
