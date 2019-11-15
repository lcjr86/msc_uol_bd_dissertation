import sys
import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from pyspark import SparkConf

from pymongo import MongoClient
from influxdb import InfluxDBClient

class ConnectAndFilter():

    def __init__(self, kafka_topic_structure, ssc, broker, load_to_db):
        self.kafka_topic_structure = kafka_topic_structure
        self.ssc = ssc
        self.broker = broker
        self.load_to_db = load_to_db

    def run(self):

        topic = self.kafka_topic_structure.replace("[SENSOR_ID]", str(i + 1))
        print("topic|" + topic)

        folder_topic = topic.replace(".", "_")
        print("folder_topic|" + folder_topic)

        ### Returns DStream
        kvs = KafkaUtils.createDirectStream(self.ssc, [topic], {"metadata.broker.list": self.broker})
        print("kvs|" + str(kvs))

        ### DStream Twith the 2nd element of the tuple
        sensor_message = kvs.map(lambda x: x[1])
        print("sensor_message|" + str(sensor_message))

        ### Filtering only the even numbers
        sensor_message_filtered = sensor_message.filter(lambda x: float(
            x.replace(re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}\|[0-9]{2}\:[0-9]{2}:[0-9]{2}\|', x)[0], "")) % 2 == 0)
        print("sensor_message_filtered|" + str(sensor_message_filtered))

        ### Print the messages
        sensor_message_filtered.pprint()

        def sendToMongoDB(rdd):
            if not rdd.isEmpty():
                message = rdd.first()
                message = message.split("|")
                client = MongoClient('mongodb://10.0.2.2:27017/')
                db = client['edge_data']
                collection = db[folder_topic]
                data = collection.insert_one({'date': message[0], 'time': message[1], 'value': message[2]})
                client.close()

        def sendToInfluxDB(rdd):
            if not rdd.isEmpty():
                message = rdd.first()
                message = message.split("|")
                client = InfluxDBClient('10.0.2.2', 8086, 'root', 'root', "edge_data")
                client.create_database(db_name)
                
                table_name = "sensor_data"

                json_body = [
                    {
                        "measurement": table_name,
                        "time": str(message[0] + "T" + message[1] + "Z"),
                        "tags": {
                            "sensorId": str(i + 1)
                        },
                        "fields": {
                            "value": str(message[2])
                        }
                    }
                ]
                print(str(json_body))
                client.write_points(json_body)

        if(load_to_db == "mongodb"):
            sensor_message_filtered.foreachRDD(lambda x: sendToMongoDB(x))

        if(load_to_db == "influxdb"):
            sensor_message_filtered.foreachRDD(lambda x: sendToInfluxDB(x))

if __name__ == "__main__":
    
    try:

        load_to_db = "influxdb"
        #load_to_db = "mongodb"

        if(load_to_db == "influxdb"):
            db_name = 'edge_data'
            client = InfluxDBClient('10.0.2.2', 8086, 'root', 'root', db_name)
            #client.drop_database(db_name)
            #client.create_database(db_name)

        number_topics = sys.argv[1]

        kafka_broker = '192.168.56.103'
        kafka_port = '9092'

        broker = kafka_broker + ':' + kafka_port
        print("broker|" + broker)

        kafka_topic_structure = 'sensor.[SENSOR_ID]'
        print("kafka_topic_structure|" + kafka_topic_structure)

        conf = SparkConf()
        conf.setMaster('yarn')
        conf.setAppName('ProcessKafkaSensorData')

        sc = SparkContext(conf=conf)
        spark = SparkSession(sc)
        ssc = StreamingContext(sc, 1)

        list_connect_and_run = []

        for i in range(0, int(number_topics)):

            print("***** " + str(i) + " *****")
            list_connect_and_run.append(ConnectAndFilter(kafka_topic_structure, ssc, broker, load_to_db))
            print("list_connect_and_run[" + str(i + 1) + "] instantiated")

        for i in range(0, int(number_topics)):

            print("***** " + str(i) + " *****")
            list_connect_and_run[i].run()
            print("list_connect_and_run[" + str(i + 1) + "].run() executed")

        ssc.start()
        ssc.awaitTermination()

    except Exception as e:
        print(e)