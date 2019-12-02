# ```/Ansible/virtualMachine/scripts/installation_configuration```

## ```00_setup_cluster_rasbian.yaml```

The responsibility of this script is to call all the support scripts that will execute the Apache Hadoop, Apache Spark, Mosquitto, Apache Kafka, Prometheus, python library dependencies and other support services (unzip) installation and configuration

That's the main playbook that will call the others on the right order.

## ```/Ansible/virtualMachine/scripts/installation_configuration/vars```

### ```parameters.yaml```

This file control some parameters that are used from some of the Ansible playbooks.