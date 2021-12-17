pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub-login')
        MASTERVM_KEY=credentials('dcdf9b28-4e9a-40d4-805a-b52ef0a6526c')
        MYSQL_ROOT_PASSWORD='QAproject21'
        MYSQL_DATABASE='dnd-database'
        MYSQL_USER='tigran@dnd-database'
        MYSQL_PWD='QAproject21'
        MYSQL_IP='dnd-database.mysql.database.azure.com'
        MYSQL_DB='dnd-database'
        MYSQL_SK='sdlkfjsdfkj'
        image="tigranargit/frontend:build-$BUILD_NUMBER"
    }
    stages {
         stage('DockerHub Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Build Frontend') {
            steps {
                sh 'docker build -t tigranargit/frontend:build-$BUILD_NUMBER /var/lib/jenkins/workspace/dndprojectpipe/frontend'
            }
        }
        stage('Push Frontend') {
            steps {
                sh 'docker push tigranargit/frontend:build-$BUILD_NUMBER'
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
               sh 'docker build -t tigranargit/database:latest /var/lib/jenkins/workspace/dndprojectpipe/database' 
            }
        }
        stage('Push Database') {
            steps {
                sh 'docker push tigranargit/database:latest'
            }
        }
        stage('Build Nginx') {
            steps {
               sh 'docker build -t tigranargit/nginx:latest /var/lib/jenkins/workspace/dndprojectpipe/nginx' 
            }
        }
        stage('Push Nginx') {
            steps {
                sh 'docker push tigranargit/nginx:latest'
            }
        }
        stage('Deploy via Docker Swarm') {
            steps {
                sh '''ssh -i $MASTERVM_KEY tigran@40.87.101.154 << EOF docker stack deploy --compose-file docker-compose.yml dndapp
                EOF
                '''
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}