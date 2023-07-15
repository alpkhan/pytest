pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python Unit_test.py'
                        
                    }
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
                        sh 'python Apply_o_olt.py'
                    }
                }
            }
        }
    }
}
