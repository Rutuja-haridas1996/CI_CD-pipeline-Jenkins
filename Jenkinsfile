pipeline {
    agent any

    stages {
        stage('Checkout...') {
            steps {
                echo 'Checkout to Documents folder..'
                sh 'cd /home/rutujaharidas/Documents' 
                sh 'ls -l'
                dir ('/home/rutujaharidas/Documents/foo') {
                    writeFile file:'dummy', text:''
                }
                sh 'ls -l'
            }
        }
        
        
        
        
        
       
        
        
    }
}
