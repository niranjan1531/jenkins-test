pipeline {
  agent any
  options { timestamps () }
  stages {
    stage('build') {
      parallel {
        stage('Task 1') {
          steps {
            sh 'pwd'
            sh 'python3 task1/run.py'
          }
        }
        stage('Task 2') {
          steps {
            sh 'ls'
            sh 'python3 task2/run.py'
          }
        }
      }
    }
    
  }
}
