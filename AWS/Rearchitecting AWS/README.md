# Journal

The next step in the devops course was to rearchitect the AWS project such that it will use more PAAS and SAAS solutions and integrate it more within AWS cloud.
I will make the following changes to the application:
-  The DataBase EC2 instance will be replaced by Amazon RDS Server
-  Memcahced EC2 instance will be replaced by ElastiCache
-  RabbitMQ will be replaced by AmazonMQ
-  Route53 will remain as DNS
-  For applications vms and combined with scaling and load balancing will use Elastic Beanstalk

## Security Groups and Keys

Before deploying any service I have once again created an SG for all of the backend services, the security key was the same I have used before in the AWS Lift and Shift project.

![SecurityGroup](https://github.com/ovimihai98/DevopsLearn/assets/138617785/b9b17021-e9f0-4a38-abd0-e8429296282d)

## RDS

The first service I deployed was the RDS (Relational Database Service)
I first created a subnet group which is sort of a network in which the database will be deployed.
Then I created a parameter group a classic one for MySQL 8.
Then I have deployed a MySQL DB and saved the admin credentials for later use in artifact creation.

![RDS](https://github.com/ovimihai98/DevopsLearn/assets/138617785/c586a498-9b34-41aa-9df8-048489e44f66)

## ElastiCache

Then I have deployed ElastiCache service on a single instance.
I have once again created a subnet group and a parameter group for the caching service.
I used memcached 1.6 version and then I have deployed the cluster (well not much of a cluster since it was just a single instance)

![Elasticache Memcache](https://github.com/ovimihai98/DevopsLearn/assets/138617785/bc5f18a4-7b7c-4a89-afac-ca4a45bbb380)

## Amazon MQ

The third and last backend service was Amazon MQ.
For it I have used the RabbitMQ option as a broker engine.
Again I have saved the admin credeantials and then deployed the service.

![rabbitmq broker](https://github.com/ovimihai98/DevopsLearn/assets/138617785/a1a77c86-bfbd-4cc3-99b8-37cb142786ff)


## Initializing DB

After the DB was fully deployed I had to run some SQL queries as per requirement of the application.
I have connected to the RDS service via a EC2 instance changed the inbound rules of RDS's SG such that I can connect with this EC2 instance, then Installed on it a mysql client (this was an ubuntu instance) then I have cloned the sourcecode and initialized the DB.

![initializing db](https://github.com/ovimihai98/DevopsLearn/assets/138617785/610177ea-6b65-4031-b75b-c539db895118)

## Beanstalk

The application was deployed on Elastic Beanstalk
Elastic Beanstalk deployed automatically EC2 instances for Tomcat8.5 with JDK.11 Application and scaled them based on autoscalling I have set.
Also deployed the loadbalancer with the URL that I wanted to set and the S3 bucket that will store the artifacts.
I also created roles for the service and for ec2 profile and set the SSH key.
The rest of the configuration was pretty self explanatory.
One special configuration was how whe application deployments will happen:
-  all at once
-  rolling
-  rolling with additional batch
-  Immutable
-  Traffic spliting
Then I have waited a bit to finish creation of the environment.

![elastic beanstalk](https://github.com/ovimihai98/DevopsLearn/assets/138617785/82f13343-8f64-4212-a4d6-f696b2976a5e)

Final step was to build and deploy the artifact. I have done it locally as I did before (clone the repo, modify the application.properties file with the parameters of the backend services and run maven) Then I have uploaded the artifact on Elastic Beanstalk.

![create-artifact](https://github.com/ovimihai98/DevopsLearn/assets/138617785/b08b432b-1740-4f58-9298-be200ba1ee8f)

The application worked as intended. Furhermore I have set my LBs URL to my domain in godaddy and the certificate in Certificate Manager so that the link will be https.
