# Pre-Configuration

To run the Ansible scripts under 'hadoop/scripts/ansible', it is important to
install ansible on the machine that will be the 'controller'

For more details about 'how to install ansible', click [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

For Mac OS, check this [link](http://techhowdy.com/install-ansible-mac-osx/).s

## ssh key generation and distribution
(create with the 'defaul user' and also with 'root')

Reference: https://www.shellhacks.com/ssh-login-without-password/

On the host machine, run: ```ssh-keygen -t rsa -b 4096 -C [your_email]```
(please also run that with the 'root' user)

then, run that to copy to the machines on the cluster:
```
ssh-copy-id [user]@[ip_machine_1]
ssh-copy-id [user]@[ip_machine_2]
...
```

- We need all the Raspberies to be able to communicate between each other without prompting for passwords. For that, we will generate SSH keys in all of them.

Ps: Please, don't forget to do that using the 'root' user as well (i.e., do it with 'pi' and 'root' users)

Also you need to copy on the rpi3 (master) to itself as well:
(ssh-copy-id root@master)

### Create the 'root' passwords

```
sudo passwd root
```

edit the file:

```
nano /etc/ssh/sshd_config```

```

adding these lines on the end:

```
PasswordAuthentication yes
PermitRootLogin yes
```

Reference: https://www.digitalocean.com/community/questions/ssh-copy-id-not-working-permission-denied-publickey