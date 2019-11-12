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

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/scenario_1_num_sensor_1.yaml'
