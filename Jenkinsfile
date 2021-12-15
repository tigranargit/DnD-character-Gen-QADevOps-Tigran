pipeline {
    agent any

    stages {
        stage('Test Frontend') {
            steps {
                cd /var/lib/jenkins/workspace/dndprojectpipe/frontend
                pip install -r ./requirements.txt
                python3 -m pytest --cov=app
            }
        }
    }
}