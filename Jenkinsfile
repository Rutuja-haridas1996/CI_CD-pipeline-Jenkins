pipeline {
    agent any
    stages {
        stage('Check Path') {
            steps {
                echo 'Check Path..'
                sh 'pwd'
            }
        }

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
        stage('Run Test file 1') {
            steps {
                echo 'Run Test App file..'
                sh 'python test.py'
            }
        }
        stage('Run Pytest file ') {
            steps {
                echo 'Run Pytest file..'
                sh 'pytest -v --tb=no'
            }
        }
        

    }

}
