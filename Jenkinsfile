pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh """
                cd /home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/venv/bin/
                source activate
                cd ..
                cd ..
                python test.py

                """

            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying at prod'
            }
        }
    }
}