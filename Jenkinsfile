pipeline {
    agent any
    stages {
        stage('Stop Nginx Server') {
            steps {
                echo 'Stop Nginx server..'
                sh 'sudo systemctl stop nginx'
            }
        }

        stage('Restart Nginx server') {
            steps {
                echo 'Restart Nginx status..'
                sh 'sudo systemctl restart nginx'

            }
        }

        stage('Check Nginx status') {
            steps {
                echo 'Check Nginx status..'
                sh 'sudo systemctl status nginx'

            }
        }

    }

}
