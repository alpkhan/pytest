pipeline {
    agent {
        docker { image 'python:3.9' }
    }

    stages {
        stage('Test') {
            steps {
                script {
                    sh 'python Unit_test.py'
                        
                    
                }
            }
        }

        stage('Config Control') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python Config_control.py'
                    }
                }
            }
        }

        stage('Deployment') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python Apply_to_olt.py'
                    }
                }
            }
        }
    }
}
