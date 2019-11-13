import sys
import re

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
from pyspark.sql.types import StringType

from pymongo import MongoClient

if __name__ == "__main__":
    
    
    try:
    
        conf = SparkConf()
        conf.setMaster('yarn')
        conf.setAppName('ProcessKafkaSensorData')

        sc = SparkContext(conf=conf)
        spark = SparkSession(sc)
        ssc = StreamingContext(sc, 1)

        brokers, topic = sys.argv[1:]
        
        folder_topic = topic.replace(".", "_")
        
        ### Returns DStream
        kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
        
        #print("kvs:", kvs)
        
        ### DStream Twith the 2nd element of the tuple
        sensor_message = kvs.map(lambda x: x[1])
        
        ### Filtering only the even numbers
        sensor_message_filtered = sensor_message.filter(lambda x: float(x.replace(re.findall('^[0-9]{4}-[0-9]{2}-[0-9]{2}\|[0-9]{2}\:[0-9]{2}:[0-9]{2}\|', x)[0], "")) % 2 == 0)
        
        ### Print the messages
        sensor_message_filtered.pprint()
        
        ### Export to MongoDB
        sensor_message_filtered.foreachRDD(lambda x: sendToMongoDB(x))
        
        def sendToMongoDB(rdd):
            if not rdd.isEmpty():
                message = rdd.first()
                message = message.split("|")
                client = MongoClient('mongodb://10.0.2.2:27017/')
                db = client['edge_data']
                collection = db[folder_topic]
                data = collection.insert_one({'date': message[0], 'time': message[1], 'value': message[2]})
                client.close()
            
        ssc.start()
        ssc.awaitTermination()
        
    except Exception as e:
        print(e)
