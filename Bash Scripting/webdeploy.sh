#!/bin/bash

USR="devops"

for host in `cat remhosts`
do
	echo "#####################################"
	echo "Connecting to $host"
	scp multios_websetup.sh $USR@$host:/tmp/
	ssh $USR@$host sudo /tmp/multios_websetup.sh
	ssh $USR@$host sudo rm -rf /tmp/multios_setup.sh
	echo "#####################################"
	echo
done
