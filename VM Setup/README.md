# Journal

So in the first day I started out by deploying VMs both manually and automatically.
For manual deployment I have used Oracle VirtualBox and the deployment is preatty easy and self explenatory.

The automated deployment howver was more interesting.
For it I had to use Vagrant and Gitbash (bcs I use a Windows PC).
Vagrant is used to easely deploy VMs on your local computer with the help of VirtualBox.
I had to create directories for every VM and use vagrant commands inside that directory to automatically setup that vm.
Some useful commands in Vagrant:
-  vagrant init "vm box name from Vagrant cloud" = for initializing Vagrant file.
-  vagrant up = creating the vm
-  vagrant status = status of the vm
-  vagrant halt = stopping the vm
-  vagrant destroy = deleting the vm
-  vagrant ssh = connecting to the vm
-  vagrant global-status = status of all vms created by vagrant.

In the repository I have attached 2 vagrant files for a centos and ubuntu servers.
