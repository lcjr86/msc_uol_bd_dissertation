# msc_uol_dissertation
This repo contain all the material related to the implementation of my dissertation

## Useful commands

System status (Linux): [Terminal $] htop

References: https://www.binarytides.com/linux-command-check-memory-usage/


# RPi_Cluster
This repo will provide all the material regarding how to setup a RaspberryPi cluster

## OS system

Between all the OS available to run on the RaspberryPi, the choose here was Raspbian.
The reasons for these choice are:
1.
2.
3.

To download the image, please click [here](https://www.raspberrypi.org/downloads/raspbian/).

Other references:
https://developer.ibm.com/recipes/tutorials/building-a-hadoop-cluster-with-raspberry-pi/

# Apache Kafka - Quickstart

Reference: https://kafka.apache.org/quickstart

## Issues regarding running in background

Reference: https://gist.github.com/piatra/0d6f7ad1435fa7aa790a


### Ansible testing:

https://docs.ansible.com/ansible/latest/reference_appendices/test_strategies.html

### under the Ansible host machine (MAC) the 'ansible.cfg' is:
```
/usr/local/Cellar/ansible
```

### Running Spark

1. Become root

```sudo -i```

2. Navegate to the spark folder

```cd /opt/hadoop/spark```

3. Start Spark

```spark-shell```

### Run simple spark test (count the number of non blank lines from a .txt file)

1. Navegate to the folder

```cd /home/hadoop```

2. Get a text as example

- Download the text

```wget -O alice.txt https://www.gutenberg.org/files/11/11-0.txt```

3. create a hdfs folder

```hdfs dfs -mkdir /inputs```

4. move the file to the hdfs folder

```hdfs dfs -put /opt/hadoop/alice.txt /inputs```

5. open Spark (check topic 'running Spark')

6. On Spark, run:

```var input = spark.read.textFile("/inputs/alice.txt")```

Then:

```input.filter(line => line.length()>0).count()```

The output should be something like: ```res0: Long = 2791```