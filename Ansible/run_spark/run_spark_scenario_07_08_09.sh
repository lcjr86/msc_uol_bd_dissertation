#!/bin/bash

cd /opt/hadoop/spark/bin
nohup spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 --master yarn --deploy-mode cluster /home/pi/Repositories/msc_uol_dissertation/Python/Data_Processing/src/main.py 4 &