pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub-login')
        MYSQL_ROOT_PASSWORD='QAproject21'
        MYSQL_DATABASE='dnd-database'
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
                sh 'docker build -t tigranargit/frontend:latest /var/lib/jenkins/workspace/dndprojectpipe/frontend'
            }
        }
        stage('Push Frontend') {
            steps {
                sh 'docker push tigranargit/frontend:latest'
            }
        }
        stage('Build Backend') {
            steps {
                sh 'docker build -t tigranargit/backend:latest /var/lib/jenkins/workspace/dndprojectpipe/backend'
            }
        }
        stage('Push Backend') {
            steps {
                sh 'docker push tigranargit/backend:latest'
            }
        }
        stage('Build Service 1') {
            steps {
                sh 'docker build -t tigranargit/service1:latest /var/lib/jenkins/workspace/dndprojectpipe/service1'
            }
        }
        stage('Push Service 1') {
            steps {
                sh 'docker push tigranargit/service1:latest'
            }
        }
        stage('Build Service 2') {
            steps {
               sh 'docker build -t tigranargit/service2:latest /var/lib/jenkins/workspace/dndprojectpipe/service2' 
            }
        }
        stage('Push Service 2') {
            steps {
                sh 'docker push tigranargit/service2:latest'
            }
        }
        stage('Build Database') {
            steps {
               sh 'docker build -t tigranargit/database:latest mysql:latest' 
            }
        }
        stage('Push Database') {
            steps {
                sh 'docker push tigranargit/database:latest'
            }
        }
        stage('Build Nginx') {
            steps {
               sh 'docker build -t tigranargit/nginx:latest nginx:latest' 
            }
        }
        stage('Push Database') {
            steps {
                sh 'docker push tigranargit/nginx:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}