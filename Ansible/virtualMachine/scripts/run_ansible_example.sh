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

ansible-playbook -i '/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/inventory_raspbian.ini' \
'/Users/lcjr86/Dropbox/MSc - Liverpool/CKIT-702--Computing Advisor Class/Implementation/msc_uol_dissertation/Ansible/virtualMachine/scripts/230_install_python3_libraries.yaml' \  
--user=root \
--ask-become-pass

