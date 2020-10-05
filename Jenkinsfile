pipeline {
    agent any

    stages {
        stage('Checkout...') {
            steps {
                echo 'Checkout to Documents folder..'
                sh 'cd /var/lib/jenkins/workspace/Pipeline Project-Demo/jenkins_project_1_Oct_05_20'
                echo 'Current location : '
                sh 'pwd'
            }
        }
        
        
        stage('Clone github repo') {
            steps {
                echo 'Clone github repo..'
                sh """cd /var/lib/jenkins/workspace/Pipeline Project-Demo/jenkins_project_1_Oct_05_20
                      git clone https://github.com/Rutuja-haridas1996/CI_CD-pipeline-Jenkins.git
                      git status
                   """
            }
        }
       
        
        
       
        
        
    }
}
