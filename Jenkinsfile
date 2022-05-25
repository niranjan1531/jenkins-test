pipeline {
  agent any
  options { timestamps () }
  stages {
    stage('build') {
      parallel {
        stage('Task 1') {
          steps {
            sh 'pwd'
            echo 'TASK 1'
            dir('task1'){
              sh 'pwd'
              sh 'ls'
              sh 'python3 task1/run.py'
            }
          }
        }
        stage('Task 2') {
          steps {
            sh 'ls'
            echo 'TASK 2'
            dir('task1'){
              sh 'pwd'
              sh 'ls'
              sh 'python3 task1/run.py'
            }
          }
        }
      }
    }
    
  }
}
