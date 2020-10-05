pipeline {
    agent any

    stages {
        stage('Install Flask') {
            steps {
                echo 'Install Flask..'
                sh 'pip install Flask'

            }
        }

        stage('Run Test file') {
            steps {
                echo 'Run Test file..'
                sh 'python test.py'

            }
        }
        stage('Run App file') {
            steps {
                echo 'Run App file..'
                sh 'python app.py'

            }
        }
       

        
    }
}
