# Implement the 'cluster' using Virtual Machines (VM)

The idea here is to test the code implementation using 2 (two) virtual machines configured to be as similar as we can to the RaspberryPis

## Virtual Machine (VM) specs

### Ubuntu Server
Virtual Machine Engine: Virtual Box
OS: Ubuntu Server 64bits
RAM: 1GB
Storage: 10GB
Processor: 1 CPU

Machine 1 name: RPi1 (OS: rpi1)
Machine 2 name: RPi2 (OS: rpi2)

### Raspian Desktop
Virtual Machine Engine: Virtual Box
OS: Debian Stretch with Raspberry Pi Desktop (Debian 9)
RAM: 1GB
Storage: 10GB (32GB for the RPi3)
Processor: 1 CPU

(depricated) Machine 1 name: RPi3 (OS: rpi3) static_ip: 192.168.56.102
Machine 1 name: RPi3_new (OS: rpi3) static_ip: 192.168.56.103
Machine 2 name: RPi4 (OS: rpi4)
Machine 3 name: RPi5 (OS: rpi5)
Machine 4 name: RPi6 (OS: rpi6)

#### Raspian configurations

> RaspberryPi Configuration > System > hostname = rpi3 (and 'rpi4', 'rpi5', ...)
> RaspberryPi Configuration > Interface > SSH: enable

## Set static IP

### on the VM with Ubuntu Server 18.04s

Reference:

https://www.codesandnotes.be/2018/10/16/network-of-virtualbox-instances-with-static-ip-addresses-and-internet-access/ (until 'Port-forwarding')

Reference:

https://www.ostechnix.com/how-to-configure-ip-address-in-ubuntu-18-04-lts/ (static IP configurations)

### on the VM with Raspian Desktop

Reference:

https://www.codesandnotes.be/2018/10/16/network-of-virtualbox-instances-with-static-ip-addresses-and-internet-access/ (until 'Port-forwarding')

Reference:

#### Setting up the static-ip (for all the machines)

1. ```sudo nano /etc/dhcpcd.conf```

2. Add on the end of the file:

```
interface eth1

static ip_address=192.168.56.<change_for_the_number_that_you_want_for_that_machine>/24
static routers=192.168.56.1
static domain_name_servers=192.168.56.1
```

https://thepihut.com/blogs/raspberry-pi-tutorials/how-to-give-your-raspberry-pi-a-static-ip-address-update

# Ansible playbooks

# Install the image from virtualbox

TO-DO: Make available the images from the VirtualBox
