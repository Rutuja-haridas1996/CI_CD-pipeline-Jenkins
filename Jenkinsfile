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
                sh 'cd /home/rutujaharidas/PycharmProjects/jenkins_3/CI_CD-pipeline-Jenkins/venv/bin/'

            }
        }
        stage('Starting virtual environment') {
            steps {
                echo 'Checkout..'
                sh 'source activate'

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
