pipeline {
    agent any

    stages {
        
        stage('Create virtual environment') {
            steps {
                echo 'Create virtual environment..'
                sh 'python3 -m venv /home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/env'

            }
        }
        stage('Activate virtual environment') {
            steps {
                echo 'Activate virtual environment..'
                sh '. /home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/env/bin/activate'

            }
        }
        stage('Install Flask') {
            steps {
                echo 'Install Flask..'
                sh 'pip install Flask'

            }
        }
        
        
        stage('Run Test file') {
            steps {
                echo 'Run App file..'
                sh 'python test.py'

            }
        }
       

        
    }
}
