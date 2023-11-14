
# AWS Lift and shift applicaiton


For this application I have followed the usual DevOps course.
This is the same project I have deployed on my VMs locally but this time on cloud
The application consists in a multitier application stack hosted on AWS services.
The stack consists in VMs for Tomcat app, Rabbit MQ, Memcache and a MySQL server. Elastic Load Balancer will be the replacement for Nginix LB, the application will be highly available

## Security Group and Keys

Before deploying vm's I have first started to deploy Security Groups for the Elastic Load Balancer, backed applications and the frontend Tomcat application
The SGs have opened ports for every app respectevely through inbound rules

![Security Groups](https://github.com/ovimihai98/DevopsLearn/assets/138617785/507ccc5f-d642-47cd-83f2-b64ef2aee8a9)

Then I have created a keypair to set public key for all my EC2s.

![KeyPair](https://github.com/ovimihai98/DevopsLearn/assets/138617785/bb518b0c-8703-457f-8d52-40e30fe4d62a)

## EC2 Instances

I have deployed one instance for every app I have used in the stack:
-  an application EC2 instance to host tomcat service
-  an EC2 instance for hosting MySQL DB
-  a RabbitMQ instance
-  a Memcache instance
The applications on the instances were deployed using user data bash scripts.
Only Tomcat instance was hosted on Ubuntu server, the others were hosted on Centos9
![ec2-instances](https://github.com/ovimihai98/DevopsLearn/assets/138617785/9f75d867-c551-4f1f-a5ad-b132b265b0bd)

I also created Route53 Records for ease of use of backend stack by Tomcat service and since maybe IPs can change over time.

![Route53 Records](https://github.com/ovimihai98/DevopsLearn/assets/138617785/2e1fd7f7-ddbb-4b15-abbc-3e46a0677e1a)

## Build and Deploy Artifacts

I have cloed the gihtub repository and build the artifact on my local machine using maven (we will learn about it later).
After the artifact was created I have created a S3 bucket but from aws cli so I needed a s3-admin account.

![s3-admin](https://github.com/ovimihai98/DevopsLearn/assets/138617785/31e0abb9-d5ea-4527-b401-2aa329fd6de8)


Then I created a S3 bucket to host the artifact WAR file in there

![s3-bucket](https://github.com/ovimihai98/DevopsLearn/assets/138617785/86dc3e39-5a39-48e0-b9d7-df08af4fc94c)

After that I have created a role and attached it to the tomcat EC2 instance so that the EC2 instance can have access to the bucket

![role-for-ec2](https://github.com/ovimihai98/DevopsLearn/assets/138617785/bf771410-5fb3-46a1-bdfd-abdd1165a9cb)


## Load Balancer and DNS

For deploying a ALB I have first created a target group and set the Tomcat EC2 instance as pending in it.

![target-group](https://github.com/ovimihai98/DevopsLearn/assets/138617785/37b29683-598d-4ee8-9954-e35df664de45)


I have then deployed the ALB. I also purchased the domain from godaddy and created a certificate from AWS Certificate Manager and linked it to the LB.

![application-lb](https://github.com/ovimihai98/DevopsLearn/assets/138617785/4f3f7b94-99d2-48b0-abc7-9a249cd3ebee)

Now the project is deployed correctly and works with https and can also be accessed via web by anyone. (cannot now because I have deleted the vms)

![project-deployed-https](https://github.com/ovimihai98/DevopsLearn/assets/138617785/73cfbaff-e99e-45ba-add1-c449e436333e)

## Autoscalling Group

For the autoscalling group I needed first a launch template for Tomcat application EC2 instance.

![launch-template-for-asg](https://github.com/ovimihai98/DevopsLearn/assets/138617785/3e64d97f-f2b9-4586-8e55-d4e9faaed4c4)

Finally I have deployed the ASG with Minimum 1 instance, recommended 1 instance and maximum 2 instances.

![Auto Scaling Group](https://github.com/ovimihai98/DevopsLearn/assets/138617785/218c1f7c-be07-4bb0-9d51-6374536f5426)



