pipeline {
    agent any
    stages {
        stage('Check Path') {
            steps {
                echo 'Check Nginx status..'
                sh 'ssh -t remotehost sudo systemctl status nginx'
            }
        }

    }

}
