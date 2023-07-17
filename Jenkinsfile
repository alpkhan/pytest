pipeline {
    agent {
        docker { image 'python:3.9' }
    }

    stages {
        stage('Test') {
            steps {
                script {
                    sh 'python Create_config.py'
                        
                    
                }
            }
        }

        stage('Config Control') {
            steps {
                script {
                    sh 'python Config_control.py'
                    
                }
            }
        }

        stage('Deployment') {
            steps {
                script {
                    sh 'python Apply_to_olt.py'
                    
                }
            }
        }
    }
}
