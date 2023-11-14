# Jorunal

This time I dive deeper into Vagrant.
I have deployed both manually and automatically 2 types of servers:
-  first one was a static website on a centos7 vm, preaty straight on there, I jsut downloaded httpd, wget, unzip and vim and downloaded a template from tooplate.com.
-  second one was a LAMP stack on a ubuntu os. This was more challenging since now I had my first error with vagrant: when the vm was provisioned, I cannot enter on it with vagrant client because it thrown me an error vagrant@127.0.0.1: Permission denied (publickey).
The error was eventually solved by login in via VirtualBox and changing sshd_config file parameter: PermitRootLogin: yes. After this issue was solved I have followed the instruction on https://ubuntu.com/tutorials/install-and-configure-wordpress#1-overview.

However the more interesting part I have learned today was the automatic provisioning of the vms trough the Vagrantfile.
I have followed the same steps as with manual provisioning but every command I have typed was inside the config.vm.provision part of the Vagrantfile of each vm. The vms files are in this repo. This was the first taste of Infrastructure as Code.
