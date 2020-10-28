pipeline {
    agent any
    stages {
        stage('Check Path') {
            steps {
                echo 'Check Nginx status..'
                sh 'sudo systemctl status nginx'
                echo '' | sudo -S  'sudo systemctl status nginx'

            }
        }

    }

}
