pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub-login')
        MYSQL_USER='tigran@dnd-database'
        MYSQL_PWD='QAproject21'
        MYSQL_IP='dnd-database.mysql.database.azure.com'
        MYSQL_DB='dnd-database'
        MYSQL_SK='sdlkfjsdfkj'
    }
    stages {
        stage('Test Frontend') {
            steps {
               sh "cd /var/lib/jenkins/workspace/dndprojectpipe/frontend"
               sh "pip3 install -r /var/lib/jenkins/workspace/dndprojectpipe/frontend/requirements.txt"
               sh "cd /var/lib/jenkins/workspace/dndprojectpipe/frontend"
               sh "python3 -m pytest"
            }
        }
        stage('Build Frontend') {
            steps {
                sh 'docker build -t frontend:latest /var/lib/jenkins/workspace/dndprojectpipe/frontend'
            }
        }
        stage('Build Backend') {
            steps {
                sh 'docker build -t backend:latest /var/lib/jenkins/workspace/dndprojectpipe/backend'
            }
        }
        stage('Build Service 1') {
            steps {
                sh 'docker build -t service1:latest /var/lib/jenkins/workspace/dndprojectpipe/service1'
            }
        }
        stage('Build Service 2') {
            steps {
               sh 'docker build -t service2:latest /var/lib/jenkins/workspace/dndprojectpipe/service2' 
            }
        }
        stage('DockerHub Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Push images to Dockerhub') {
            steps {
                sh 'docker push frontend:latest'
                sh 'docker push backend:latest'
                sh 'docker push service1:latest'
                sh 'docker push service2:latest'
            }
        }
        stage('Remove created images locally') {
            steps {
                sh 'docker rmi frontend:latest backend:latest service1:latest service2:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}