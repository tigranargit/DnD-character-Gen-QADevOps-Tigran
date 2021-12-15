pipeline {
    agent any
    stages {
        stage('Test Frontend') {
            steps {
               sh "cd /var/lib/jenkins/workspace/dndprojectpipe/frontend"
               sh "pip3 install -r ./requirements.txt"
               sh "python3 -m pytest --cov=app"
            }
        }
    }
}