pipeline {
    agent any
    environment {
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
               sh "python3 -m pytest tests --cov=frontend"
            }
        }
    }
}