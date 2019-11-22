### All the libraries that are used on the script
import sys
import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from pyspark import SparkConf

from pymongo import MongoClient
from influxdb import InfluxDBClient

from datetime import datetime, timedelta

class ConnectAndFilter():
    '''
        ConnectAndFilter class:
            Description: 
                This class is responsable to :
                1. Get the data from Kafka (kafka topic)
                2. Process the data:
                    The data input is a message (sring) that contains a random integer on the interval [1, 10].
                    Example of message (data input): "2019-11-16|20:52:09|4"
                        (Note that the last information (let's call 'value'), after "|" is the integer mentioned before)
                    For each message, the 'value' will be extracted and filtered.
                    The filter is: 'value' % 2 == 0 , i.e., checks if 'value' is a even number.
                3. Load the processed data to the DataBase (by default: "influxDB") on the Data Center.
                    (Note that the DataBase on the Data Center is emulated on the localhost machine, running the choosen DB)
    '''

    def __init__(self, kafka_topic_structure, ssc, broker, load_to_db):
        '''
            Parameters:
                kafka_topic_structure:
                    Description: The structure of the topic name
                    Type: String
                    Example: sensor/[SENSOR_ID]
                ssc:
                    Description: Spark streaming context
                    Type: object
                    More details: https://spark.apache.org/docs/2.1.3/api/python/pyspark.streaming.html
                broker:
                    Description: Broker address + port
                    Type: String
                    Example: "192.168.56.103:9092"
                load_to_db:
                    Description: name of the database that you would like to load the filtered / processed data
                    Type: String
                    Example: "influxdb" or "mongodb"
        '''

        ### Get the values (on the instantiation of the object)
        self.kafka_topic_structure = kafka_topic_structure
        self.ssc = ssc
        self.broker = broker
        self.load_to_db = load_to_db

    def run(self, sensorId):
        
        ### get the sensorId (ex:1 or 2 or etc...)
        self.sensorId = sensorId

        ### get the topic name, based on the sensorId reference
        self.topic = self.kafka_topic_structure.replace("[SENSOR_ID]", str(self.sensorId + 1))
        #print("topic|" + topic)

        ### Get the Kafka Direct Stream (based on the Spark Streaming context and Kafka details, like topic and broker address)
        kvs = KafkaUtils.createDirectStream(self.ssc, [self.topic], {"metadata.broker.list": self.broker})
        #print("kvs|" + str(kvs))

        ### Direct Stream Twith the 2nd element of the tuple
        sensor_message = kvs.map(lambda x: x[1])
        #print("sensor_message|" + str(sensor_message))

        ### Applying the filtering
        sensor_message_filtered = sensor_message.filter(lambda x: float(
            x.replace(re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}\|[0-9]{2}\:[0-9]{2}:[0-9]{2}\|', x)[0], "")) % 2 == 0)
        #print("sensor_message_filtered|" + str(sensor_message_filtered))

        ### Print the messages
        #sensor_message_filtered.pprint()

        ### send the data to MongoDB method
        def sendToMongoDB(rdd):
            '''
                Parameters:
                    rdd:
                        Description: Resilient Distributed Dataset
                        Type: Object
                        More details: https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html
                                    
            '''            
            
            ### check if the stream is not null
            if not rdd.isEmpty():
                
                ### Get the message
                message = rdd.first()

                ### Split the message in multiples parts (by "|")
                message = message.split("|")

                ### Create the MongoDB client
                client = MongoClient('mongodb://10.0.2.2:27017/')
                
                ### Create the database 'edge_data'
                db = client['edge_data']

                ### Create the MongoDB collection (based on the topic name)
                collection = db[self.topic.replace(".", "_")]

                ### Upload the data from 'message' following the structure:
                ### example: {'date': '2019-11-16', 'time': '20:52:09', 'value': '4'}
                data = collection.insert_one({'date': message[0], 'time': message[1], 'value': message[2]})
                
                ### close the client
                client.close()

        ### send the data to InfluxDB method
        def sendToInfluxDB(rdd):
            '''
                Parameters:
                    rdd:
                        Description: Resilient Distributed Dataset
                        Type: Object
                        More details: https://spark.apache.org/docs/1.1.1/api/python/pyspark.rdd.RDD-class.html
                                    
            '''

            ### check if the stream is not null
            if not rdd.isEmpty():

                ### Get the message
                message = rdd.first()

                ### Split the message in multiples parts (by "|")
                message = message.split("|")

                ### Create the MongoDB collection (based on the topic name)
                client = InfluxDBClient('10.0.2.2', 8086, 'root', 'root', "edge_data")

                ### Create the database 'edge_data'
                client.create_database(db_name)
                
                ### Define the table name
                table_name = "sensor_data"

                ### Define the data that will be insert on the InfluxDB

                ### Adjust the date to the UTC time (Influx purpose)
                date_temp = message[0] + "T" + message[1] + "Z"
                date_temp = datetime.strptime(date_temp, "%Y-%m-%dT%H:%M:%SZ")
                date_temp = date_temp - timedelta(hours=1, minutes=0)

                json_body = [
                    {
                        "measurement": table_name,
                        "time": str(date_temp),
                        "tags": {
                            "sensorId": str(self.sensorId + 1)
                        },
                        "fields": {
                            "value": str(message[2]),
                            "tic": 1
                        }
                    }
                ]
                #print(str(json_body))
                
                ### Insert the data
                client.write_points(json_body)

        ### Select, base on the value of the variable 'load_to_db' with DB will be used
        if(load_to_db == "mongodb"):
            sensor_message_filtered.foreachRDD(lambda x: sendToMongoDB(x))

        if(load_to_db == "influxdb"):
            sensor_message_filtered.foreachRDD(lambda x: sendToInfluxDB(x))

if __name__ == "__main__":
    
    try:
        
        ### Define the variable 'load_to_db'
        load_to_db = "influxdb"
        #load_to_db = "mongodb"

        ### Some extra steps if 'load_to_db == "influxdb"'
        if(load_to_db == "influxdb"):
            db_name = 'edge_data'
            client = InfluxDBClient('10.0.2.2', 8086, 'root', 'root', db_name)

        ### Get the number of topics that will be processed (pass on the execution of the script, by the command line)
        number_topics = sys.argv[1]

        ### Define Kafka details (broker, port, topic_structure, etc...)
        kafka_broker = '192.168.56.103'
        kafka_port = '9092'

        broker = kafka_broker + ':' + kafka_port
        #print("broker|" + broker)

        kafka_topic_structure = 'sensor.[SENSOR_ID]'
        #print("kafka_topic_structure|" + kafka_topic_structure)

        ### Create the Spark Configuration Object
        conf = SparkConf()

        ### Set on the Spark Configuration 'YARN" as framework used to process the job
        conf.setMaster('yarn')

        ### Set the Application Name
        conf.setAppName('ProcessKafkaSensorData')

        ### Create the Spark Context based on the configuration define previously
        sc = SparkContext(conf=conf)

        ### Create the Spark Session (using the Spark Context define previously)
        spark = SparkSession(sc)

        ### Create the Stream Context (using the Spark Context define previously and the frequency = 1s)
        ssc = StreamingContext(sc, 1)

        ### Create a list that will 'store' the "ConnectAndFilter()" objects
        list_connect_and_run = []

        ### Based on the number of topics, loop and define the "ConnectAndFilter" objects
        for i in range(0, int(number_topics)):

            #print("***** " + str(i) + " *****")
            list_connect_and_run.append(ConnectAndFilter(kafka_topic_structure, ssc, broker, load_to_db))
            #print("list_connect_and_run[" + str(i + 1) + "] instantiated")

        ### Based on the number of topics, loop and execute the "ConnectAndFilter" run method
        for i in range(0, int(number_topics)):

            #print("***** " + str(i) + " *****")
            list_connect_and_run[i].run(i)
            #print("list_connect_and_run[" + str(i + 1) + "].run() executed")

        ### Start and "put in loop" the execution of the Streamming Context
        ssc.start()
        ssc.awaitTermination()

    except Exception as e:
        print(e)