from kafka import KafkaProducer

import configparser
import logging
from logging.config import fileConfig

fileConfig('../config/logging.ini')
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()
config.read('../config/setup.ini')

### Initial information for the kafka Broker
kafka_broker = config['kafka']['broker_address']
kafka_port = config['kafka']['broker_port']
kafka_topic = config['kafka']['topic_structure'].replace("[SENSOR_ID]", "1")

### Create the MQTT Broker connector
kafka_producer = KafkaProducer(bootstrap_servers=[kafka_broker + ':' + kafka_port])

future = kafka_producer.send(kafka_topic, b'py-test')
result = future.get(timeout=60)