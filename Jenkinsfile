pipeline {
    agent any
    stages {
        stage('Test Frontend') {
            steps {
               sh "sudo apt install python3 pip3 pytest"
               sh "cd /var/lib/jenkins/workspace/dndprojectpipe/frontend"
               sh "pip3 install -r ./requirements.txt"
               sh "python3 -m pytest --cov=app"
            }
        }
    }
}