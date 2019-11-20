### Import the relevant libraries for that script
import logging
from logging.config import fileConfig
import random
import configparser


### Get the logging configuration file
fileConfig('../config/logging.ini')

### Instantiate the logger object
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()

### Load the file to the config handlers
config.read('../config/setup.ini')

class sensor():
    '''
        This class will basically implement the method that will generate the sensors data
    '''
    def __init__(self):
        '''
            values that are set on the instantiation of the sensor object
        '''
        try:

            ### Get the seed (from the configuration file) to initialize the random number generator
            self.seed = config['sensor']['seed']

            ### Initialize the random number generator
            random.seed(self.seed)

            logger.info('sensor class instantiated')

        except Exception as e:
            logger.exception(e)

    def generateData(self):
        '''
            Method that will generate the data (random int numbers between 1 and 10)
            "For integers, there is uniform selection from a range"
            More details: https://docs.python.org/3.7/library/random.html
        '''
        try:
            ### Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)
            return random.randint(1, 10)
        except Exception as e:
            logger.exception(e)
