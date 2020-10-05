pipeline {
    agent any

    stages {
        stage('Checkout...') {
            steps {
                echo 'Checkout to Documents folder..'
                sh 'cd /home/rutujaharidas/Documents'
                echo 'Current location : '
                sh 'pwd'
            }
        }
        
        
        stage('Make directory') {
            steps {
                sh 'cd /home/rutujaharidas/Documents'
                echo 'Make directory..'
                sh 'mkdir /home/rutujaharidas/Documents/jenkins_project_1_Oct_05_20'
                sh 'pwd'
                sh 'cd /home/rutujaharidas/Documents/jenkins_project_1_Oct_05_20'

            }
        }
        
        
        
       
        
        
    }
}
