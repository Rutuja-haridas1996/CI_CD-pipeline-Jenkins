pipeline {
    agent any

    stages {
        stage('Define bash') {
            steps {
                echo 'Checkout..'
                sh '#!/bin/bash'

            }
        }

        stage('Checkout to Venv') {
            steps {
                echo 'Checkout..'
                sh 'python test.py'

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
