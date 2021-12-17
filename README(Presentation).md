# DnD App CI/CD implementation

# Set up:

- Code in VSC on my local machine with a GitHub repositoty integration
- GitHub webhook triggering Jenkins pipeline with every push
- Jenkins VM
- Master VM
- Worker VM
- DockerHub
- Jira for project management

# The process:

The app is divided into services: frontend, backend, service1, service2, database and nginx.

The frontend undergoes unit testing via a testing stage in Jenkins pipeline. I managed to make it work once (screenshots provided), but due to the issues with code scanning, had to remove that stage from my final pipeline in order to allow all other stages to go ahead.

All services have a respective Dockerfile used to create images from within a jenkins script found in Jenkinsfile. 
 
The Jenkins VM is separate to the other two VMs. The Master VM is set up as a docker swarm manager and the Worker VM is set up as a worker node. Master VM contains a docker-compose.yml file used to deploy the services simultaneously as a stack.

Services run on 5000, 5001, 5002 and 5003 ports, while nginx acts as a reverse proxy on port 80, being the only point of access for the users. The database was implemented using Azure MySQL.

# Jenkins pipeline:

 1. Test the front end
 2. Build each service one by one for easy error detection
 3. Login to DockerHub
 4. Push each image to DockerHub
 5. SSH into the Master VM
 6. Deploy the services as a stack 
 7. Log out of the DockerHub


















To make Jenkins ssh

sudo su into jenkins vm
create a .pem file of the same name as the second VM and copy the pem contents into it
ssh into the vm while sudo su as jenkins 

add the pem key into jenkins credentials 
add the credential to jenkinfule env.variable 
use the cred as follows: $CRED_NAME

to ssh into a vm via jenkinsfile:

sh 'ssh -i $MASTERVM_KEY tigran@40.87.101.154 << EOF docker stack deploy --compose-file docker-compose.yml EOF' -second EOF is probs optional

might also do all the steps the dude did in the youtube video:

putting the .pem into var/lib/jenkins and chown the file to jenkins:jenkins 