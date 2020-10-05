pipeline {
    agent any

    stages {
        
        stage('Create virtual environment') {
            steps {
                echo 'Create virtual environment..'
                sh 'python3 -m venv venv'

            }
        }
        stage('Activate virtual environment') {
            steps {
                echo 'Activate virtual environment..'
                sh '. venv/bin/activate'

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
