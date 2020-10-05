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
                echo 'Make directory..'
                sh 'mkdir jenkins_project_1_Oct_05_20'

            }
        }
        stage('Checkout to project folder') {
            steps {
                echo 'checkout to project folder..'
                sh 'cd jenkins_project_1_Oct_05_20'
                echo 'Currenet location'
                sh 'pwd'
            }
        }
        
        
        stage('Clone Github repository') {
            steps {
                echo 'Clone Github repo..'
                sh 'git clone https://github.com/Rutuja-haridas1996/CI_CD-pipeline-Jenkins.git'

            }
        }
        
        stage('Git status') {
            steps {
                echo 'Git status..'
                sh 'git status'

            }
        }
        
        
        
    }
}
