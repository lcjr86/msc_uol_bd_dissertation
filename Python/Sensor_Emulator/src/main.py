import logging
from logging.config import fileConfig
import emulator as e
import configparser
import os

### Define the root directory path
ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

### Get the logging configuration file
fileConfig(os.path.join(ROOT_DIR, 'config', 'logging.ini'))

### Instantiate the logger object
logger = logging.getLogger()

logger.info('Running emulator')

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()

### Load the file to the config handlers
config.read(os.path.join(ROOT_DIR, 'config', 'setup.ini'))

### Get the 'frequency in seconds' and also the 'number of sensors' from the setup.ini file
frequency_in_seconds = config["emulator"]["frequency_in_seconds"]
numSensors = config["emulator"]["numSensors"]

### Define if you are publishing to the MQTT broker (local = False) or not (local = True)
local = False

### Define if you are saving the MQTT messages the the influxDB
store_db = True

### Instantiate the emulator
emulator = e.emulator(frequency_in_seconds, numSensors, local, store_db)

### Run the emulator
emulator.run()