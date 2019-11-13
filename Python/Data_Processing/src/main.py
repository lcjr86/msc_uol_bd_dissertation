

import logging
from logging.config import fileConfig

import configparser

import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from pyspark import SparkConf

from pymongo import MongoClient

from os import path

logging_INI_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/logging.ini')

fileConfig(logging_INI_file_path)
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()

setup_INI_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/setup.ini')

config.read(setup_INI_file_path)

number_topics = config['Global']['num_topics']
logger.info("number_topics|" + number_topics)

class sparkMainSession():

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic

        conf = SparkConf()
        conf.setMaster('yarn')
        conf.setAppName('ProcessKafkaSensorData')

        self.sc = SparkContext(conf=conf)
        self.spark = SparkSession(self.sc)
        self.ssc = StreamingContext(self.sc, 1)

        folder_topic = self.topic.replace(".", "_")

    def send_to_mongodb(self, rdd):

        if not rdd.isEmpty():
            message = rdd.first()
            message = message.split("|")
            client = MongoClient('mongodb://10.0.2.2:27017/')
            db = client['edge_data']
            collection = db[self.folder_topic]
            data = collection.insert_one({'date': message[0], 'time': message[1], 'value': message[2]})
            client.close()

    def connect_and_filter(self):

        ### Returns DStream
        kvs = KafkaUtils.createDirectStream(self.ssc, [self.topic], {"metadata.broker.list": self.brokers})


        # print("kvs:", kvs)

        ### DStream Twith the 2nd element of the tuple
        sensor_message = kvs.map(lambda x: x[1])

        ### Filtering only the even numbers
        sensor_message_filtered = sensor_message.filter(lambda x: float(
            x.replace(re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}\|[0-9]{2}\:[0-9]{2}:[0-9]{2}\|', x)[0], "")) % 2 == 0)

        ### Print the messages
        sensor_message_filtered.pprint()

        ### Export to MongoDB
        sensor_message_filtered.foreachRDD(lambda x: self.send_to_mongodb(x))

        self.ssc.start()
        self.ssc.awaitTermination()

if __name__ == "__main__":

    try:

        kafka_broker = config['kafka']['broker_address']
        logger.info("kafka_broker|" + kafka_broker)

        kafka_port = config['kafka']['broker_port']
        logger.info("kafka_port|" + kafka_port)

        kafka_topic_structure = config['kafka']['topic_structure']
        logger.info("kafka_topic_structure|" + kafka_topic_structure)

        list_sparkMainSession  = []

        for i in range(0, int(number_topics)):

            broker = kafka_broker + ':' + kafka_port
            topic = kafka_topic_structure.replace("[SENSOR_ID]", str(i + 1))

            list_sparkMainSession.append(sparkMainSession(broker, topic))
            logger.info("list_sparkMainSession[" + str(i) + "] created")

        for i in range(0, int(number_topics)):

            list_sparkMainSession[i].connect_and_filter()
            logger.info("list_sparkMainSession[" + str(i) + "].connect_and_filter() executed")

    except Exception as e:
        logger.exception(e)