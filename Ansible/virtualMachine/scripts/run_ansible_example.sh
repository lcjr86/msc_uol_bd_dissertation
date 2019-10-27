#!/bin/bash


### My Professional Mac
# ansible-playbook -i /Users/luizcarlosdejesusjunior/Documents/Repos/RPi_Cluster/virtualMachine/scripts/ansible/inventory_ubuntu_server.ini \
# /Users/luizcarlosdejesusjunior/Documents/Repos/RPi_Cluster/virtualMachine/scripts/ansible/00_setup_hadoop_cluster.yaml \
# --user=root \
# --ask-become-pass

ansible-playbook -i /Users/luizcarlosdejesusjunior/Documents/Repos/RPi_Cluster/virtualMachine/scripts/ansible/inventory_rasbian.ini \
/Users/luizcarlosdejesusjunior/Documents/Repos/RPi_Cluster/virtualMachine/scripts/ansible/00_setup_hadoop_cluster_raspbian.yaml \
--user=root \
--ask-become-pass

### My Personal Mac
# ansible-playbook -i /Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/inventory_ubuntu_server.ini \
# /Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/00_setup_hadoop_cluster.yaml \
# --user=root \
# --ask-become-pass

ansible-playbook -i /Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/inventory_raspbian.ini \
/Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/00_setup_hadoop_cluster_rasbian.yaml \
--user=root \
--ask-become-pass

#### install MQTT Broker and Client

ansible-playbook -i /Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/inventory_raspbian.ini \
/Users/lcjr86/Dropbox/RPi_Cluster/SBC_Master/MQTT_Broker/ansible/00_install_Mosquitto.yaml \
--user=root \
--ask-become-pass

#### install Apache Nifi

# ansible-playbook -i /Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/inventory_raspbian.ini \
# /Users/lcjr86/Dropbox/RPi_Cluster/SBC_Master/Apache_Nifi/ansible/10_install_Apache_Nifi-1-8-0.yaml \
# --user=root \
# --ask-become-pass


#### set Apache Kafka

ansible-playbook -i /Users/lcjr86/Dropbox/RPi_Cluster/virtualMachine/scripts/ansible/inventory_raspbian.ini \
/Users/lcjr86/Dropbox/RPi_Cluster/SBC_Master/Apache_Kafka/ansible/00_set_apache_kafka.yaml \
--user=root \
--ask-become-pass