pipeline {
  agent any
  
    environment {
        PATH = "C:\\Windows\\System32;C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    }
    
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Comcomeng/projek-uas'
      }
    }

    stage('Build Docker') {
      steps {
        echo 'Building Docker image...'
        dir('task-service') {
          bat 'docker build -t task-service .'
        }
      }
    }

    stage('Run Tests') {
      steps {
        echo 'Running tests...'
        dir('task-service') {
          bat 'docker run --rm task-service pytest'
        }
      }
    }
  }

  post {
    failure {
      echo 'Build Gagal!'
    }
  }
}
