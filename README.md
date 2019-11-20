# msc_uol_dissertation

This repo contain all the material related to the implementation of my dissertation

## /Ansible

### /Ansible/hadoop_2-7-7

Configuration files used to configure Apache Hadoop 2.7.7

### /Ansible/host

All the Ansible playbooks used to install, configure and run:

- Prometheus
- Grafana
- InfluxDB

### /Ansible/MQTT_Kafka_bridge

Files that will be use to adjust the ```Python/MQTT_Kafka_bridge``` script to run the right 'test case scenario'

### /Ansible/run_spark

Few scripts that illustrates how to run the (py)Spark Data_processing scripts on the cluster (master node)

### /Ansible/Sensor_Emulator

Files that will be use to adjust the ```Python/Sensor_Emulator``` script to run the right 'test case scenario'

### /Ansible/virtualMachine

All the Ansible playbooks used to install, configure and run:

- Hadoop
- MQTT Broker
- Kafka
- Spark
- Prometheus exporters

## /Python

### /Python/Clean_influxDB

Application that will clean the 'influxDB' db: 'edge_data'. (Related to the run of the 'test case scenarios')

### /Python/Data_Processing

(py)Spark code that will process the data from the Kafka Broker "in real time"

### /Python/MQTT_Kafka_bridge

Application that will subscribe to the MQTT topics and pubish the messages to Kafka topics

### /Python/Sensor_Emulator

Sensor emulator will be able to generate random data, emulating one or multiples sensors

### /Python/simple_influxDB_test

Simple full end-to-end example of how to use influxDB with Python

### /Python/simple_pySpark_test

Simple example of the usage of (py)Spark, with Spark running under YARN/HADOOP

# RPi_Cluster

This repo will provide all the material regarding how to setup a RaspberryPi cluster

## OS system

Between all the OS available to run on the RaspberryPi, the choose here was Raspbian.

To download the image, please click [here](https://www.raspberrypi.org/downloads/raspbian/).

## References:

https://developer.ibm.com/recipes/tutorials/building-a-hadoop-cluster-with-raspberry-pi/
https://www.linode.com/docs/databases/hadoop/how-to-install-and-set-up-hadoop-cluster/
https://www.linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/


#### Others

## Useful commands

System status (Linux): [Terminal $] htop

References: https://www.binarytides.com/linux-command-check-memory-usage/
