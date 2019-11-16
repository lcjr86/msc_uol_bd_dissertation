#!/bin/bash

## My Personal Mac

### Set Cluster
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/00_setup_cluster_rasbian.yaml' --user=root --ask-become-pass

#### start Local
ansible-playbook '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/host/scripts/00_start_host_services.yaml' --user=root --ask-become-pass


### scenario_1

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_1__00_num_sensor_1.yaml'  --user=root --ask-become-pass

##### Run 'sensor_emulator'
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_1__50_run_sensor_emulator.yaml'  --user=root --ask-become-pass


#### scenario_2

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_2__00_num_sensor_2.yaml'  --user=root --ask-become-pass

##### Run 'sensor_emulator'
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_2__50_run_sensor_emulator.yaml'  --user=root --ask-become-pass


#### scenario_3

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_3__00_num_sensor_4.yaml'  --user=root --ask-become-pass

##### Run 'sensor_emulator'
ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_3__50_run_sensor_emulator.yaml'  --user=root --ask-become-pass
