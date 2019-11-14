import sys
import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from pyspark import SparkConf

from pymongo import MongoClient

if __name__ == "__main__":
    
    try:

        def sendToMongoDB(rdd):
            if not rdd.isEmpty():
                message = rdd.first()
                message = message.split("|")
                client = MongoClient('mongodb://10.0.2.2:27017/')
                db = client['edge_data']
                collection = db[folder_topic]
                data = collection.insert_one({'date': message[0], 'time': message[1], 'value': message[2]})
                client.close()

        conf = SparkConf()
        conf.setMaster('yarn')
        conf.setAppName('ProcessKafkaSensorData')

        sc = SparkContext(conf=conf)
        spark = SparkSession(sc)
        ssc = StreamingContext(sc, 1)

        number_topics = sys.argv[1]

        kafka_broker = '192.168.56.103'
        kafka_port = '9092'

        broker = kafka_broker + ':' + kafka_port
        print("broker|" + broker)

        kafka_topic_structure = 'sensor.[SENSOR_ID]'
        print("kafka_topic_structure|" + kafka_topic_structure)

        ssc.start()
        print("ssc started")

        ssc.awaitTermination()
        print("ssc awaitTermination")

        for i in range(0, int(number_topics)):

            print("***** " + str(i) + " *****")

            topic = kafka_topic_structure.replace("[SENSOR_ID]", str(i + 1))
            print("topic|" + topic)

            folder_topic = topic.replace(".", "_")
            print("folder_topic|" + folder_topic)

            ### Returns DStream
            kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})
            print("kvs|" + str(kvs))

            ### DStream Twith the 2nd element of the tuple
            sensor_message = kvs.map(lambda x: x[1])
            print("sensor_message|" + str(sensor_message))

            ### Filtering only the even numbers
            sensor_message_filtered = sensor_message.filter(lambda x: float(x.replace(re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}\|[0-9]{2}\:[0-9]{2}:[0-9]{2}\|', x)[0], "")) % 2 == 0)
            print("sensor_message_filtered|" + str(sensor_message_filtered))

            ### Print the messages
            sensor_message_filtered.pprint()

            ### Export to MongoDB
            sensor_message_filtered.foreachRDD(lambda x: sendToMongoDB(x))
        
    except Exception as e:
        print(e)
