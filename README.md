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

!()[./cicddiagram.png]

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



# DnD-Character-Gen

This is a simple microservice application built using flask.

Application is designed so that users can enter the frontend service on port 5000 while leaving the other three services only accessible through the frontend.

## Requirements

| Service Name | Port |
| ------------ | ---- |
| frontend | 5000 |
| service1 | 5001 |
| service2 | 5002 |
| backend | 5003 |

'frontend' service needs environment variables named:

- MYSQL_USER
- MYSQL_PWD
- MYSQL_IP - endpoint of mysql database
- MYSQL_DB - schema name
- MYSQL_SK - random string of letters and numbers (genuinely doesn't matter)

Also need a mysql database with a blank schema initialised (flask app will create tables and dummy data)

