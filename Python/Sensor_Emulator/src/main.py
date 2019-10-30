import logging
from logging.config import fileConfig
import emulator as e
import configparser

fileConfig('../config/logging.ini')
logger = logging.getLogger()
logger.info('Running emulator')


### Get the 'setup.ini' file handler
config = configparser.ConfigParser()
config.read('../config/setup.ini')

### Get the 'frequency in seconds' and also the 'number of sensors' from the setup.ini file
frequency_in_seconds = config["emulator"]["frequency_in_seconds"]
numSensors = config["emulator"]["numSensors"]

### Define if you are publishing to the MQTT broker (local = False) or not (local = True)
local = False

### Instantiate the emulator

emulator = e.emulator(frequency_in_seconds, numSensors, local)

### Run the emulator
emulator.run()