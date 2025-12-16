pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "your_dockerhub_username"  #this is docker hub user#
        IMAGE_NAME = "user-service"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your/repo.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    sh "docker build -t $DOCKERHUB_USER/$IMAGE_NAME ."
                }
            }
        }

        stage('Docker Push') {
            steps {
                script {
                    sh "docker login -u $DOCKERHUB_USER -p $DOCKERHUB_TOKEN"
                    sh "docker push $DOCKERHUB_USER/$IMAGE_NAME"
                }
            }
        }
    }
}
