pipeline {
    agent any

    stages {
        stage('Install Flask') {
            steps {
                echo 'Checkout..'
                sh 'pip install Flask'

            }
        }

        stage('Run Test file') {
            steps {
                echo 'Checkout..'
                sh 'python test.py'

            }
        }
        stage('Run App file') {
            steps {
                echo 'Checkout..'
                sh 'python app.py'

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
