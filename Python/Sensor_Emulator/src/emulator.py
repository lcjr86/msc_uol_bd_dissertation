
import time
import logging
from logging.config import fileConfig
import paho.mqtt.client as paho
import time
import datetime
import configparser
import os
from influxdb import InfluxDBClient

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

    def __init__(self, frequency_in_seconds, numSensors, local, store_db):
        self.frequency_in_seconds = int(frequency_in_seconds)
        self.numSensors = int(numSensors)
        self.local = local
        self.store_db = store_db

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

            if self.store_db:
                db_name = 'sensor_data'
                client = InfluxDBClient('localhost', 8086, 'root', 'root', db_name)
                client.drop_database(db_name)
                client.create_database(db_name)

            ### Generate the data and print
            while True:

                timestamp = datetime.datetime.fromtimestamp(time.time())

                for i in range(0, self.numSensors):

                    data = listSensors[i].generateData()

                    if self.local:

                        message = "sensor_" + str(i + 1) + "|" + str(
                            timestamp.strftime('%Y-%m-%d|%H:%M:%S')) + "|" + str(data)

                        print(message)

                    else:

                        message = str(
                            timestamp.strftime('%Y-%m-%d|%H:%M:%S')) + "|" + str(data)

                        ### create a topic for each sensor
                        topic = topic_structure.replace("[SENSOR_ID]", str(i + 1))
                        ### publish the data to the topic
                        mqtt_broker_client.publish(topic, message)

                        logger.info("topic|" + str(topic) + "|message|" + message)


                    if self.store_db:

                        table_name = "sensor_data"
                        date_format = '%Y-%m-%dT%H:%M:%S%Z'

                        json_body = [
                            {
                                "measurement": table_name,
                                "time": str(timestamp.strftime(date_format) + "Z"),
                                "tags": {
                                    "sensorId": str(i + 1)
                                },
                                "fields": {
                                    "value": data
                                }
                            }
                        ]

                        client.write_points(json_body)

                        logger.info("data inserted on db: " + db_name + "table: " + table_name)
                        logger.info("data inserted:" + str(json_body))

                time.sleep(self.frequency_in_seconds)

        except Exception as e:
            logger.exception(e)


