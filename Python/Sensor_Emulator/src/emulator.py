
import time
import logging
from logging.config import fileConfig
import paho.mqtt.client as paho
import time
import datetime
import configparser
import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

#fileConfig('../config/logging.ini')
fileConfig(os.path.join(ROOT_DIR, 'config', 'logging.ini'))
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()
#config.read('../config/setup.ini')
config.read(os.path.join(ROOT_DIR, 'config', 'setup.ini'))

import sensor as s

class emulator:

    def __init__(self, frequency_in_seconds, numSensors, local):
        self.frequency_in_seconds = int(frequency_in_seconds)
        self.numSensors = int(numSensors)
        self.local = local

    def run(self):
        try:

            logger.info('Emulator run triggered')

            ### instanteate the sensors
            listSensors = []
            for i in range(0, self.numSensors):
                listSensors.append(s.sensor())

            ### if is not running local, create the client that connects to the MQTT broker
            if not self.local:
                broker = config['mosquitto']['broker_address']
                port = int(config['mosquitto']['broker_port'])
                topic_structure = config['mosquitto']['topic_structure']
                mqtt_broker_client = paho.Client("sensor_Emulator")
                mqtt_broker_client.connect(broker, port)

            ### Generate the data and print
            while True:

                if self.local:
                    for i in range(0, self.numSensors):
                        message = "sensor_" + str(i + 1) + "|" + str(
                            datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d|%H:%M:%S')) + "|" + str(
                            listSensors[i].generateData())

                        print(message)
                else:
                    for i in range(0, self.numSensors):

                        message = str(
                            datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d|%H:%M:%S')) + "|" + str(
                            listSensors[i].generateData())

                        ### create a topic for each sensor
                        topic = topic_structure.replace("[SENSOR_ID]", str(i + 1))
                        ### publish the data to the topic
                        mqtt_broker_client.publish(topic, message)

                        logger.info("topic|" + str(topic) + "|message|" + message)

                time.sleep(self.frequency_in_seconds)

        except Exception as e:
            logger.exception(e)


