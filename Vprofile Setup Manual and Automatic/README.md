# Journal

Today I have deployed social media mock application on my PC both manually setup and automatic setup.
I have used the repository provided by the instructor from the DevOps course.

The application consists in a Nginx frontend server used as Load balancer, a Tomcat application server (mainly because the app was written in Java), Mysql database, RabbitMQ message broker and Memcached caching server.

First I have ran the Vagrantfile to provision all of the servers, then I have started to configure them one by one starting from the bottom of backend and making my way towards the frontend:
1.  MYSQL Setup
  -  hosted on a centos vm, I have installed MariaDB service, ran the installation script, and then cloned the source code from github and initialized the db.
2.  Memcache Setup
  -  hosted on centos vm, I have installed and enabled memcache service
3.  RabbitMQ Setup
  -  hosted on a centos vm, I have installed dependencies and enabled the service. Also I have created a test user to make it admin for the service.
4.  Tomcat Setup
  -  hosted on a centos vm, I have installed java dependencies, git maven wget.
  -  downloaded tomcat package
  -  created a tomcat service user
  -  setup systemctl for tomcat
  -  cloned the source code from github and updated the application.properties file with backend details
  -  build the code with maven
5.  Nginx setup
  -  hosted on an ubuntu vm, installed nginx and configured the conf file for the connection with tomcat server.

At the end the service ran successfully.

After manual provisioning of the file, I have then setup the application automatically using Vagrant and bash scripts for every service.
