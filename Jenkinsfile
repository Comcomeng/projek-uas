pipeline {
  agent any

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
          bat 'pytest'
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
