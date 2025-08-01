pipeline {
  agent any

  environment {
    PATH = "C:\\Windows\\System32;C:\\Program Files\\Docker\\Docker\\resources\\bin;${env.PATH}"
    SONARQUBE_SERVER = 'sonarqube' // Ganti dengan nama SonarQube server yg kamu isi di Jenkins config
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

    stage('SonarQube Analysis') {
      steps {
        echo 'Running SonarQube analysis...'
        dir('task-service') {
          withSonarQubeEnv("${env.SONARQUBE_SERVER}") {
            bat 'sonar-scanner -Dsonar.projectKey=task-service -Dsonar.projectName="Task Service UAS" -Dsonar.sources=.'
          }
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
