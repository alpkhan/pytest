pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'pip install -r requirements.txt'  // If you have any requirements
                        sh 'python test.py'
                    }
                }
            }
        }

        stage('Code Control') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python control.py'
                    }
                }
            }
        }

        stage('Deployment') {
            steps {
                script {
                    docker.image('python:3.9').inside {
                        sh 'python depl.py'
                    }
                }
            }
        }
    }
}
