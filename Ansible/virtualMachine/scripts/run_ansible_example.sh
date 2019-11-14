#!/bin/bash


### My Professional Mac

#### Cluster
ansible-playbook -i /Users/luizcarlosdejesusjunior/Documents/Repos/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini \
/Users/luizcarlosdejesusjunior/Documents/Repos/msc_uol_dissertation/Ansible/virtualMachine/scripts/00_setup_cluster_rasbian.yaml \
--user=root \
--ask-become-pass

### My Personal Mac

#### Set Cluster
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/00_setup_cluster_rasbian.yaml' --user=root --ask-become-pass

#### start Local
ansible-playbook '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/host/scripts/00_start_host_services.yaml' --user=root --ask-become-pass



#### scenario_1

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_1_num_sensor_1.yaml'  --user=root --ask-become-pass

##### Run MQTT_Kafka_bridge
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_1__run_mqtt_kafka_bridge.yaml'  --user=root --ask-become-pass

##### Run PySpark script
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_1__run_pyspark_script.yaml'  --user=root --ask-become-pass


#### scenario_2

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_2_num_sensor_2.yaml'  --user=root --ask-become-pass



#### scenario_3

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_3_num_sensor_5.yaml'  --user=root --ask-become-pass