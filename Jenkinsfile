pipeline {
    agent any

    stages {
        stage('Checkout...') {
            steps {
                echo 'Checkout to Documents folder..'
                sh 'cd home/rutujaharidas/Documents'
                echo 'Current location : '
                sh 'pwd'
            }
        }
        
        
        stage('Make directory') {
            steps {
                echo 'Make directory..'
                sh 'mkdir -p home/rutujaharidas/Documents/jenkins_project_1_Oct_05_20'

            }
        }
        stage('Checkout to project folder and git clone') {
            steps {
                echo 'checkout to project folder..'
                sh 'cd /home/rutujaharidas/Documents/jenkins_project_1_Oct_05_20'
                echo 'Current location'
                sh 'pwd'
                sh 'git clone https://github.com/Rutuja-haridas1996/CI_CD-pipeline-Jenkins.git'
                
            }
        }
        
        
       
        
        
    }
}
