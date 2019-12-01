# ```/Ansible/virtualMachine/scripts/test_case_scenarios```

### ```scenario_all__30_clean_infludb_edge_data.yaml```

Playbook that clean/delete the influxDB 'edge_data' on the host PC.
This script is called by ```__scenario_01_02_03.yaml```, ```__scenario_04_05_06.yaml``` and ```__scenario_07_08_09.yaml```

## ```__scenario_01_02_03.yaml```

Playbook responsable to 'call' the following scripts:

### ```scenario_01_02_03__10_create_kafka_topic.yaml```

Playbook responsable to create 1 kafka topic.

### ```scenario_01_02_03__20_run_mqtt_kafka_bridge.yaml```

Playbook responsable to run "MQTT-Kafka bridge" for 1 topic.

## ```__scenario_04_05_06.yaml```

Playbook responsable to 'call' the following scripts:

### ```scenario_04_05_06__10_create_kafka_topic.yaml```

Playbook responsable to create 2 kafka topics.

### ```scenario_04_05_06__20_run_mqtt_kafka_bridge.yaml```

Playbook responsable to run "MQTT-Kafka bridge" for 2 topics.

## ```__scenario_07_08_09.yaml```

Playbook responsable to 'call' the following scripts:

### ```scenario_07_08_09__10_create_kafka_topic.yaml```

Playbook responsable to create 4 kafka topics.

### ```scenario_07_08_09__20_run_mqtt_kafka_bridge.yaml```

Playbook responsable to run "MQTT-Kafka bridge" for 4 topics.

## Run Sensor Emulator

## ```_scenario_01_s1_t5__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 1;
- Frequency for the data generation: each 5 seconds.

## ```_scenario_02_s1_t15__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 1;
- Frequency for the data generation: each 15 seconds.

## ```_scenario_03_s1_t60__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 1;
- Frequency for the data generation: each 60 seconds.

## ```_scenario_04_s2_t5__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 2;
- Frequency for the data generation: each 5 seconds.

## ```_scenario_05_s2_t15__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 2;
- Frequency for the data generation: each 15 seconds.

## ```_scenario_06_s2_t60__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 2;
- Frequency for the data generation: each 60 seconds.

## ```_scenario_07_s4_t5__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 4;
- Frequency for the data generation: each 5 seconds.

## ```_scenario_08_s4_t15__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 4;
- Frequency for the data generation: each 15 seconds.

## ```_scenario_09_s4_t60__50_run_sensor_emulator.yaml```

Playbook responsable to run the "sensor emulator" with the following configuration:
- Number of sensors: 4;
- Frequency for the data generation: each 60 seconds.


## ```/Ansible/virtualMachine/scripts/test_case_scenarios/vars```

### ```parameters.yaml```

This file control some parameters that are used from some of the Ansible playbooks.