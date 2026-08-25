pipeline {

    agent any

    triggers {
        githubPush()
    }

    environment {
        AWS_REGION = "ap-south-1"
        ECR_REGISTRY = "583749796090.dkr.ecr.ap-south-1.amazonaws.com"
        ECR_REPOSITORY = "devops-app"
        IMAGE_NAME = "${ECR_REGISTRY}/${ECR_REPOSITORY}"
        SONAR_SCANNER_HOME = tool 'SonarQubeScanner'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                    ./venv/bin/python -m py_compile app.py
                    ./venv/bin/python -m pytest
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        export PATH="$SONAR_SCANNER_HOME/bin:$PATH"

                        sonar-scanner \
                        -Dsonar.projectKey=Flask-Production-CI-CD \
                        -Dsonar.projectName="Flask Production CI/CD" \
                        -Dsonar.sources=.
                    '''
                }
            }
        }

        stage('Configure EKS') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'aws-credentials',
                        usernameVariable: 'AWS_ACCESS_KEY_ID',
                        passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                    )
                ]) {
                    sh '''
                        export AWS_DEFAULT_REGION=${AWS_REGION}

                        mkdir -p $HOME/.kube

                        aws eks update-kubeconfig \
                          --region ${AWS_REGION} \
                          --name devops-eks \
                          --kubeconfig $HOME/.kube/config

                        kubectl config current-context
                        kubectl get nodes
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                '''
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'aws-credentials',
                        usernameVariable: 'AWS_ACCESS_KEY_ID',
                        passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                    )
                ]) {
                    sh '''
                        export AWS_DEFAULT_REGION=${AWS_REGION}

                        aws ecr get-login-password \
                        --region ${AWS_REGION} | \
                        docker login \
                        --username AWS \
                        --password-stdin ${ECR_REGISTRY}
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                '''
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh '''
                    kubectl set image deployment/devops-app \
                    devops-app=${IMAGE_NAME}:${BUILD_NUMBER}

                    kubectl rollout status deployment/devops-app
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl get pods -l app=devops-app
                    kubectl get deployment devops-app
                    kubectl get svc devops-app-service
                '''
            }
        }
    }
}
