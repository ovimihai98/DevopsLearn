I have learned this past week more about AWS cloud.
I already have the Cloud Practicioner Certifcation so I know my ways trough AWS.
First I have deployed EC2 instances. I have deployed Ubuntu/Centos9/AmazonLinux instances, I have created security groups that are like firewalls for EC2s and also created ssh keypairs to login to those vms. For the security groups I have set inbound rules to open the ssh port.
Good to know: Security groups are statefull, analyze traffic both inbound and outbound.
EC2 instances have both a private and a public IP, so I have deployed a static website, opened port 80 for http on SG for my IP and I could see the website on the browser.
public IPs can change every time EC2 instance is rebooting, for this a variant is to allocate a static IP for a EC2 instance such that it will always have that IP assigned. But this is not a good option and a better one is to use a Load Balancer.
You can also open aditional volumes which are additional virtual hard drives assigned to a EC2.
I have also used AWS CLI to deploy an EC2 using a dedicated IAM user.
EBS or Elastic Block Storage is a block-storage designed for EC2.
I ahve also deployed an Elastic Load Balancer which is used to distribute incoming traffic accross multiple targets, in our case was EC2 instances. There are more types of ELBs but I have deployed the Application Load Balancer that routes traffic based on the application level of the OSI model.
I learned about CloudWatch which monitors AWS environment and metrics (logs).
I have deployed an auto scalling group which is a set of instruction you set for EC2 instances to deploy based on different metrics (loads).
Learned about S3 storage, which is preatty straight forward, also with a twist since you can enable versioning and also can deploy a static website on it.
Lastly I learned about RDS database. I don't know very much about databases so most of what I understood from it is that RDS is the DB SAAS service offered by AWS.

All of these will be used later in a project in which I will deploy the application that I have deployed locally in the cloud both using IAAS and SAAS.
