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
         stage('DockerHub Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Build Frontend') {
            steps {
                sh 'sudo docker build -t frontend:latest /var/lib/jenkins/workspace/dndprojectpipe/frontend'
            }
        }
        stage('Push Frontend') {
            steps {
                sh 'docker push frontend:latest'
            }
        }
        stage('Remove Frontend locally') {
            steps {
                sh 'docker rmi frontend:latest' 
            }
        }
        stage('Build Backend') {
            steps {
                sh 'docker build -t backend:latest /var/lib/jenkins/workspace/dndprojectpipe/backend'
            }
        }
        stage('Push Backend') {
            steps {
                sh 'docker push backend:latest'
            }
        }
        stage('Remove Backend locally') {
            steps {
                sh 'docker rmi backend:latest' 
            }
        }
        stage('Build Service 1') {
            steps {
                sh 'docker build -t service1:latest /var/lib/jenkins/workspace/dndprojectpipe/service1'
            }
        }
        stage('Push Service 1') {
            steps {
                sh 'docker push service1:latest'
            }
        }
        stage('Remove Service 1 locally') {
            steps {
                sh 'docker rmi service1:latest' 
            }
        }
        stage('Build Service 2') {
            steps {
               sh 'docker build -t service2:latest /var/lib/jenkins/workspace/dndprojectpipe/service2' 
            }
        }
        stage('Push Service 2') {
            steps {
                sh 'docker push service2:latest'
            }
        }
        stage('Remove Service 2 locally') {
            steps {
                sh 'docker rmi service2:latest' 
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}