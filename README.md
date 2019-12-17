# msc_uol_dissertation

This repo contain all the material related to the implementation of my dissertation.

## ```/Ansible```

### ```/Ansible/hadoop_2-7-7```

Configuration files used to configure Apache Hadoop 2.7.7.

### ```/Ansible/host```

All the Ansible playbooks used to install, configure and run:

- Prometheus;
- Grafana;
- InfluxDB.

### ```/Ansible/MQTT_Kafka_bridge```

Files that will be use to adjust the ```Python/MQTT_Kafka_bridge``` script to run the right 'test case scenario'

### ```/Ansible/run_spark```

Few scripts that illustrates how to run the (py)Spark Data_processing scripts on the cluster (master node)

### ```/Ansible/Sensor_Emulator```

Files that will be use to adjust the ```Python/Sensor_Emulator``` script to run the right 'test case scenario'

### ```/Ansible/virtualMachine```

All the Ansible playbooks used to install, configure and run:

- Hadoop;
- MQTT Broker;
- Kafka;
- Spark;
- Prometheus exporters.

## ```/Python```

### ```/Python/Clean_influxDB```

Application that will clean the 'influxDB' db: 'edge_data' (Related to the run of the 'test case scenarios').

### ```/Python/Data_Processing```

(py)Spark code that will process the data from the Kafka Broker "in real time".

### ```/Python/MQTT_Kafka_bridge```

Simple MQTT (Mosquitto) -> Kafka bridge. Publish in a MQTT topic and have you message republished into a Kafka topic.

### ```/Python/Sensor_Emulator```

Sensor emulator will be able to generate random data, emulating one or multiples sensors.

### ```/Python/simple_influxDB_test```

Simple full end-to-end example of how to use influxDB with Python.

### ```/Python/simple_pySpark_test```

Simple example of the usage of (py)Spark, with Spark running under YARN/HADOOP.

## ```/Test_Case_Scenarios_Results```

All the results (screenshots + .xls with the numbers) collected from the monitoring tool for each test case scenario executed.

# ---------

# Implement the 'cluster' using Virtual Machines (VM)

The idea here is to test the code implementation using 3 (two) virtual machines configured to be as similar as we can to the RaspberryPis

## Virtual Machine (VM) specs

### Raspian Desktop

- Virtual Machine Engine: Virtual Box
- OS: Debian Stretch with Raspberry Pi Desktop (Debian 9)
- RAM: 2GB
- Storage: 10GB (32GB for the RPi3)
- Processor: 1 CPU

#### Machine Details

- Machine 1 name: RPi3_new (OS: rpi3) static_ip: 192.168.56.103
- Machine 2 name: RPi4 (OS: rpi4) static_ip: 192.168.56.202
- Machine 3 name: RPi5 (OS: rpi5) static_ip: 192.168.56.203

#### Raspian configurations

- RaspberryPi Configuration > System > hostname = rpi3 (and 'rpi4', 'rpi5', ...)
- RaspberryPi Configuration > Interface > SSH: enable

## Set static IP

### on the VM with Raspian Desktop

#### Setting up the static-ip (for all the machines)

1. ```sudo nano /etc/dhcpcd.conf```

2. Add on the end of the file:

```
interface eth1

static ip_address=192.168.56.<change_for_the_number_that_you_want_for_that_machine>/24
static routers=192.168.56.1
static domain_name_servers=192.168.56.1
```

## References:


- https://www.codesandnotes.be/2018/10/16/network-of-virtualbox-instances-with-static-ip-addresses-and-internet-access/ (until 'Port-forwarding')


- https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-give-your-raspberry-pi-a-static-ip-address-update


- https://developer.ibm.com/recipes/tutorials/building-a-hadoop-cluster-with-raspberry-pi/

- https://www.linode.com/docs/databases/hadoop/how-to-install-and-set-up-hadoop-cluster/

- https://www.linode.com/docs/databases/hadoop/install-configure-run-spark-on-top-of-hadoop-yarn-cluster/
