import logging
from logging.config import fileConfig
import emulator as e
import configparser
import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

#fileConfig('../config/logging.ini')
fileConfig(os.path.join(ROOT_DIR, 'config', 'logging.ini'))
logger = logging.getLogger()
logger.info('Running emulator')

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()
#config.read('../config/setup.ini')
config.read(os.path.join(ROOT_DIR, 'config', 'setup.ini'))

### Get the 'frequency in seconds' and also the 'number of sensors' from the setup.ini file
frequency_in_seconds = config["emulator"]["frequency_in_seconds"]
numSensors = config["emulator"]["numSensors"]

### Define if you are publishing to the MQTT broker (local = False) or not (local = True)
local = False

### Instantiate the emulator

emulator = e.emulator(frequency_in_seconds, numSensors, local)

### Run the emulator
emulator.run()