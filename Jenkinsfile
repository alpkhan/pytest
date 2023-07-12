pipeline {
    agent none
    stages {
        stage('Unit Test') {
            agent {
                docker {
                    image 'python:3.9' // Replace with your desired Python Docker image
                }
            }
            steps {
                sh 'pip install -r requirements.txt' // Install dependencies
                sh 'python unit.py' // Run unit tests
            }
        }

        stage('Code Control') {
            agent {
                docker {
                    image 'python:3.9' // Replace with your desired Python Docker image
                }
            }
            steps {
                sh 'python code.py' // Perform code control steps
            }
        }

        stage('Deployment') {
            agent {
                docker {
                    // Specify the Docker image for deployment if needed
                }
            }
            steps {
                // Deploy the application
                // Add the deployment steps based on your deployment process
            }
        }
    }
}
