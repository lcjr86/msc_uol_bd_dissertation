### Import the relevant libraries
import logging
from logging.config import fileConfig
import paho.mqtt.client as paho

from kafka import KafkaProducer

import configparser

#### Get the configuration file for the logging
fileConfig('../config/logging.ini')

### Instantiate the logger object
logger = logging.getLogger()

### Get the 'setup.ini' file handler
config = configparser.ConfigParser()

### Load the file to the config handler
config.read('../config/setup.ini')

### Get the number of topics that will be processed
number_topics = config['Global']['num_topics']
logger.info("number_topics|" + number_topics)

class Bridge():
    '''
        This class will implement the bridge between MQTT and Kafka broker
        (It is assuming that the topics are created on both brokers)
        1. Create the MQTT broker connectors
        2. Create the KAFKA broker connectors
        3. Subscribe to the MQTT broker topics
        4. Publish the messages (from the MQTT broker topics) to the Kafka topics
    '''

    def run(self):
        '''
            This method will do all the steps described previously
        '''
        try:

            ### Get the MQTT broker address
            mqtt_broker = config['mosquitto']['broker_address']
            logger.info("mqtt_broker|" + mqtt_broker)
            #print("mqtt_broker|" + mqtt_broker)

            ### Get the MQTT broker port
            mqtt_port = int(config['mosquitto']['broker_port'])
            logger.info("mqtt_port|" + str(mqtt_port))
            #print("mqtt_port|" + str(mqtt_port))

            ### Get the MQTT broker topic name structure
            mqtt_topic_structure = config['mosquitto']['topic_structure']
            logger.info("mqtt_topic_structure|" + mqtt_topic_structure)
            #print("mqtt_topic_structure|" + mqtt_topic_structure)

            ### Get the Kafka broker address
            kafka_broker = config['kafka']['broker_address']
            logger.info("kafka_broker|" + kafka_broker)
            #print("kafka_broker|" + kafka_broker)

            ### Get the Kafka broker port
            kafka_port = config['kafka']['broker_port']
            logger.info("kafka_port|" + kafka_port)
            #print("kafka_port|" + kafka_port)

            ### Get the Kafka broker topic name structure
            kafka_topic_structure = config['kafka']['topic_structure']
            logger.info("kafka_topic_structure|" + kafka_topic_structure)
            #print("kafka_topic_structure|" + kafka_topic_structure)

            ### Initiate the lists that will 'host':
            ### - MQTT topic names
            ### - Kafka topic names
            ### - MQTT broker client (object)
            list_mqtt_topic = []
            list_kafka_topic = []
            list_mqtt_broker_client = []

            ### this loop will 'load' the lists defined above
            for i in range(0, int(number_topics)):
                
                ### Insert the MQTT topic name to the appropriated list
                list_mqtt_topic.append(mqtt_topic_structure.replace("[SENSOR_ID]", str(i + 1)))
                logger.info("mqtt_topic["+str(i)+"]|" + list_mqtt_topic[i])
                #print("mqtt_topic["+str(i)+"]|" + list_mqtt_topic[i])

                ### Insert the Kafka topic name to the appropriated list
                list_kafka_topic.append(kafka_topic_structure.replace("[SENSOR_ID]", str(i + 1)))
                logger.info("kafka_topic["+str(i)+"]|" + list_kafka_topic[i])
                #print("kafka_topic["+str(i)+"]|" + list_kafka_topic[i])

                ### Create the MQTT Broker connector client and append to the appropriate list
                list_mqtt_broker_client.append(MQTTClient("sensor_" + str(i + 1)))
                logger.info("mqtt_broker_client["+str(i)+"] created")
                #print("mqtt_broker_client["+str(i)+"] created")

            ### list that will 'host' the Kafka producers (object)
            list_kafka_producer = []

            ### This loop will:
            ### 1. Connect to the MQTT client
            ### 2. Subscribe to the MQTT topic
            ### 3. Append the Kafka producers to the appropriated list
            for i in range(0, int(number_topics)):

                ### Connet to the MQTT brokers
                list_mqtt_broker_client[i].connect(mqtt_broker, mqtt_port)
                logger.info("mqtt_broker_client["+str(i)+"].connect executed")
                #print("mqtt_broker_client["+str(i)+"].connect executed")

                ### Subscribe to the MQTT broker topics
                list_mqtt_broker_client[i].subscribe(list_mqtt_topic[i])
                logger.info("mqtt_broker_client["+str(i)+"].subscribe executed")
                #print("mqtt_broker_client["+str(i)+"].subscribe executed")

                ### Append the Kafka producers to the appropriated list
                list_kafka_producer.append(KafkaProducer(bootstrap_servers=[kafka_broker + ':' + kafka_port]))
                logger.info("KafkaProducer["+str(i)+"] executed")
                #print("KafkaProducer["+str(i)+"] executed")

            ### Create an empty list based on the number of topics that will be processed
            list_future = [None] * int(number_topics)

            ### Global variable with the message from the topics that was subscribed
            global subscribe_message

            ### Get the message from the MQTT Broker and publish to the Kafka topic
            while True:
                
                ### Instantiate this list that will hold the messages from the topics
                list_subscribe_message = [None] * int(number_topics)

                ### This loop will:
                ### - start the subscription looping request
                ### - check if there is a message
                ### - publish the message to the equivalent Kafka topic
                for i in range(0, int(number_topics)):

                    logger.info("***** " + str(i) + " *****")
                    #print("***** " + str(i) + " *****")

                    ### Start the MQTT topic subscription loop
                    list_mqtt_broker_client[i].loop_start()
                    logger.info("mqtt_broker_client["+str(i)+"].loop_start executed")
                    #print("mqtt_broker_client["+str(i)+"].loop_start executed")

                    ### Check if the message is not empty
                    if(list_mqtt_broker_client[i].subscribe_message != ""):

                        logger.info("subscribe_message|" + str(list_mqtt_broker_client[i].subscribe_message))
                        #print("subscribe_message|" + str(list_mqtt_broker_client[i].subscribe_message))

                        logger.info("list_kafka_topic["+str(i)+"]|" + list_kafka_topic[i])
                        #print("list_kafka_topic["+str(i)+"]|" + list_kafka_topic[i])

                        ### send the message to the equivalent Kafka topic
                        list_future[i] = list_kafka_producer[i].send(list_kafka_topic[i], list_mqtt_broker_client[i].subscribe_message)
                        #print("list_future["+str(i)+"]|" + str(list_future[i]))

                        ### kafka-sys output handler
                        result = list_future[i].get(timeout=60)

                        ### Set subscribe_message = "" to avoid publish the same message multiple times
                        list_mqtt_broker_client[i].set_subscribe_message_as_message_consumed()

                    ### stop the subscription loop
                    list_mqtt_broker_client[i].loop_stop()
                    logger.info("mqtt_broker_client.loop_stop executed")
                    #print("mqtt_broker_client.loop_stop executed")

        except Exception as e:
            logger.exception(e)
            #print(e)

class MQTTClient():
    '''
        (Re)Implementation of the MQTTClient.
        The objetive is to be able to handle the message (output of the MQTT submission topic) properly.
    '''

    ### Start the variable with an empty value
    subscribe_message = ""

    def __init__(self, client_name):
        '''
            Parameters:
                client_name:
                    Description: MQTT Broker client name
                    Type: String
                    Example: "sensor_1"
        '''
        ### Set the MQTT broke client
        self.client = paho.Client(client_name)
        
        ### (re)define the "on_message" method
        self.client.on_message = self.on_message

    def connect(self, broker, port):
        '''
            (Re)Implement the MQTT Broker Client 'connect' method
        '''
        self.client.connect(broker, port)

    def subscribe(self, topic):
        '''
            (Re)Implement the MQTT Broker Client 'subscribe' method
        '''        
        self.client.subscribe(topic)

    def on_message(self, client, userdata, message):
        '''
            (Re)Implement the MQTT Broker Client 'subscribe' method
        '''       
        try:
            
            ### Get the subscribe message (from the 'on_message' method) and set to the 'subscribe_message' variable
            self.subscribe_message = str.encode(message.payload.decode("utf-8"))            

        except Exception as e:
            print(e)

    def loop_start(self):
        '''
            (Re)Implement the MQTT Broker Client 'loop_start' method
        '''               
        self.client.loop_start()

    def loop_stop(self):
        '''
            (Re)Implement the MQTT Broker Client 'loop_stop' method
        '''                      
        self.client.loop_stop()

    def set_subscribe_message_as_message_consumed(self):
        '''
            Implement a method that set 'subscribe_message' to empty
        '''              
        self.subscribe_message = ""
