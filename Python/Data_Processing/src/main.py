import spark_filter_kafka_to_mongodb as s

### Instantiate the emulator
spark = s.filterKafkaMongoDB()

### Run the emulator
spark.run()