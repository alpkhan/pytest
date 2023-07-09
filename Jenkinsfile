pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh echo "TESTTTT"
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'python3 ilk.py'
      }
    }
  }
}
