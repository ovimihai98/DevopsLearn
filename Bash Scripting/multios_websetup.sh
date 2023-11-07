#!/bin/bash


#Variable Declaration
#PACKAGE="httpd unzip wget"
#SVC="httpd"
URL="https://www.tooplate.com/zip-templates/2130_waso_strategy.zip"
ART_NAME="2130_waso_strategy"
TEMPDIR="/tmp/webfiles"

yum --help &> /dev/null

if [ $? -eq 0 ]
then
	
	echo "Running Setup on CentOS"
	PACKAGE="httpd unzip wget"
	SVC="httpd"
	#Installing Dependencies

	sudo yum install $PACKAGE -y > /dev/null

	#Start and Enable Service

	sudo systemctl start $SVC
	sudo systemctl enable $SVC


	#Creating temp directory
	mkdir -p $TEMPDIR
	cd $TEMPDIR
	
	wget $URL > /dev/null
	unzip $ART_NAME.zip > /dev/null
	sudo cp -r $ART_NAME/* /var/www/html/

	#Restart service
	sudo systemctl restart $SVC
	ls /var/www/html/

else
	echo "Running Setup on Ubuntu"
        PACKAGE="apache2 unzip wget"
        SVC="apache2"
        #Installing Dependencies
	sudo apt update
        sudo apt install $PACKAGE -y > /dev/null

        #Start and Enable Service

        sudo systemctl start $SVC

        #Creating temp directory
        mkdir -p $TEMPDIR
        cd $TEMPDIR

        wget $URL > /dev/null
        unzip $ART_NAME.zip > /dev/null
        sudo cp -r $ART_NAME/* /var/www/html/

        #Restart service
        sudo systemctl restart $SVC
        ls /var/www/html/
fi
