

import logging
from logging.config import fileConfig
import paho.mqtt.client as paho

from kafka import KafkaProducer

import configparser

fileConfig('../config/logging.ini')
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()
config.read('../config/setup.ini')

number_topics = config['Global']['num_topics']
logger.info("number_topics|" + number_topics)

class bridge:

    def __init__(self):
        pass

    def run(self):
        try:

            ### Initial information for the MQTT Broker
            mqtt_broker = config['mosquitto']['broker_address']
            logger.info("mqtt_broker|" + mqtt_broker)
            print("mqtt_broker|" + mqtt_broker)

            mqtt_port = int(config['mosquitto']['broker_port'])
            logger.info("mqtt_port|" + str(mqtt_port))
            print("mqtt_port|" + str(mqtt_port))

            mqtt_topic_structure = config['mosquitto']['topic_structure']
            logger.info("mqtt_topic_structure|" + mqtt_topic_structure)
            print("mqtt_topic_structure|" + mqtt_topic_structure)

            kafka_broker = config['kafka']['broker_address']
            logger.info("kafka_broker|" + kafka_broker)
            print("kafka_broker|" + kafka_broker)

            kafka_port = config['kafka']['broker_port']
            logger.info("kafka_port|" + kafka_port)
            print("kafka_port|" + kafka_port)

            kafka_topic_structure = config['kafka']['topic_structure']
            logger.info("kafka_topic_structure|" + kafka_topic_structure)
            print("kafka_topic_structure|" + kafka_topic_structure)

            list_mqtt_topic = []
            list_kafka_topic = []
            list_mqtt_broker_client = []

            for i in range(0, int(number_topics)):

                list_mqtt_topic.append(mqtt_topic_structure.replace("[SENSOR_ID]", str(i + 1)))
                logger.info("mqtt_topic["+str(i)+"]|" + list_mqtt_topic[i])
                print("mqtt_topic["+str(i)+"]|" + list_mqtt_topic[i])

                list_kafka_topic.append(kafka_topic_structure.replace("[SENSOR_ID]", str(i + 1)))
                logger.info("kafka_topic["+str(i)+"]|" + list_kafka_topic[i])
                print("kafka_topic["+str(i)+"]|" + list_kafka_topic[i])

                ### Create the MQTT Broker connector
                # list_mqtt_broker_client.append(paho.Client("sensor_" + str(i + 1)))
                # logger.info("mqtt_broker_client["+str(i)+"] created")
                # print("mqtt_broker_client["+str(i)+"] created")

                ### Create the MQTT Broker connector
                list_mqtt_broker_client.append(MQTTClient("sensor_" + str(i + 1)))
                logger.info("mqtt_broker_client["+str(i)+"] created")
                print("mqtt_broker_client["+str(i)+"] created")

            list_kafka_producer = []

            for i in range(0, int(number_topics)):

                list_mqtt_broker_client[i].connect(mqtt_broker, mqtt_port)
                logger.info("mqtt_broker_client["+str(i)+"].connect executed")
                print("mqtt_broker_client["+str(i)+"].connect executed")

                list_mqtt_broker_client[i].subscribe(list_mqtt_topic[i])
                logger.info("mqtt_broker_client["+str(i)+"].subscribe executed")
                print("mqtt_broker_client["+str(i)+"].subscribe executed")

                list_kafka_producer.append(KafkaProducer(bootstrap_servers=[kafka_broker + ':' + kafka_port]))
                logger.info("KafkaProducer["+str(i)+"] executed")
                print("KafkaProducer["+str(i)+"] executed")

                # list_mqtt_broker_client[i].on_message = on_message  # attach function to callback
                # logger.info("mqtt_broker_client["+str(i)+"].on_message executed")
                # print("mqtt_broker_client["+str(i)+"].on_message executed")

            ### Create an empty list based on the number of topics
            list_future = [None] * int(number_topics)
            global subscribe_message

            ### Get the message from the MQTT Broker and publish to the Kafka topic
            while True:

                list_subscribe_message = [None] * int(number_topics)

                for i in range(0, int(number_topics)):

                    print("***** " + str(i) + " *****")

                    list_mqtt_broker_client[i].loop_start()
                    logger.info("mqtt_broker_client["+str(i)+"].loop_start executed")
                    print("mqtt_broker_client["+str(i)+"].loop_start executed")

                    # list_subscribe_message[i] = subscribe_message
                    # logger.info("list_subscribe_message["+str(i)+"]|" + str(list_subscribe_message[i]))
                    # print("list_subscribe_message["+str(i)+"]|" + str(list_subscribe_message[i]))

                    if(list_mqtt_broker_client[i].subscribe_message != ""):

                        logger.info("subscribe_message|" + str(list_mqtt_broker_client[i].subscribe_message))
                        print("subscribe_message|" + str(list_mqtt_broker_client[i].subscribe_message))

                        logger.info("list_kafka_topic["+str(i)+"]|" + list_kafka_topic[i])
                        print("list_kafka_topic["+str(i)+"]|" + list_kafka_topic[i])

                        list_future[i] = list_kafka_producer[i].send(list_kafka_topic[i], list_mqtt_broker_client[i].subscribe_message)
                        print("list_future["+str(i)+"]|" + str(list_future[i]))

                        result = list_future[i].get(timeout=60)

                        #print("result|" + str(result))

                        ### Set subscribe_message = "" to avoid publish the same message multiple times
                        list_mqtt_broker_client[i].set_subscribe_message_as_message_consumed()

                    list_mqtt_broker_client[i].loop_stop()
                    logger.info("mqtt_broker_client.loop_stop executed")
                    print("mqtt_broker_client.loop_stop executed")


        except Exception as e:
            logger.exception(e)
            print(e)



class MQTTClient():

    subscribe_message = ""

    def __init__(self, client_name):
        self.client = paho.Client(client_name)
        self.client.on_message = self.on_message

    def connect(self, broker, port):
        self.client.connect(broker, port)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def on_message(self, client, userdata, message):

        try:

            #print(str.encode(message.payload.decode("utf-8")))
            self.subscribe_message = str.encode(message.payload.decode("utf-8"))

        except Exception as e:
            print(e)

    def loop_start(self):
        self.client.loop_start()

    def loop_stop(self):
        self.client.loop_stop()

    def set_subscribe_message_as_message_consumed(self):
        self.subscribe_message = ""
