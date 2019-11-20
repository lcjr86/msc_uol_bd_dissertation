# MQTT_Kafka_bridge

## /Python/MQTT_Kafka_bridge/config/

### logging.ini

Configuration file that handles the log configuration (formating, structure, etc...).

### setup.ini

Configuration file that handles:

- The number of the topics;
- Mosquitto (MQTT Broker) configuration;
- Kafka Broker configuration.

## /Python/MQTT_Kafka_bridge/log/

### info.log

All the logging when the ```../src/main.py``` is executed

## /Python/MQTT_Kafka_bridge/src/

### main.py

The MQTT - Kafka bridge execution

### bridge.py

The MQTT - Kafka bridge code implementation

## /Python/MQTT_Kafka_bridge/old/

Old scripts that were used for test purposes.

## /Python/MQTT_Kafka_bridge/venv/

Python virtual environment folder

### Others - Apache Kafka - Quickstart

Reference: https://kafka.apache.org/quickstart

#### Others - Issues regarding running in background

Reference: https://gist.github.com/piatra/0d6f7ad1435fa7aa790a