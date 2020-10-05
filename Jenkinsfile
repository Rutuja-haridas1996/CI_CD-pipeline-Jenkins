pipeline {
    agent any

    stages {
        
        stage('Make directory') {
            steps {
                echo 'Make directory..'
                sh 'mkdir new_jenkins_project'

            }
        }
        stage('Clone github repo') {
            steps {
                echo 'Clone github repo..'
                sh 'git clone https://github.com/Rutuja-haridas1996/CI_CD-pipeline-Jenkins.git'

            }
        }
        
    }
}
