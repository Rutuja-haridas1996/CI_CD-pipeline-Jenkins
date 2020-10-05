pipeline {
    agent any

    stages {
        
        stage('Starting virtual environment') {
            steps {
                echo 'Checkout..'
                sh '. ./venv/bin/activate'

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
