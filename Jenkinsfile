// Define variable
//def myVariable = "foo"
def doc_workspace = "/home/rutujaharidas/Documents"



pipeline {
    agent any

    stages {
        stage('Checkout...') {
            steps {
                echo 'Checkout to Documents folder..'
                echo "${doc_workspace}"
                sh 'dir("${doc_workspace}/aQA"){
                    sh "pwd"
                }'
            }

        }
        
        
        
        
        
       
        
        
    }
}
