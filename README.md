# Flask Production CI/CD with AWS EKS

A production-style DevOps project demonstrating automated CI/CD, containerization, Kubernetes deployment, AWS cloud infrastructure, database integration, security, monitoring, and application observability.

## 🚀 Project Overview

This project implements a Flask REST API with PostgreSQL database integration and deploys it on Amazon EKS.

The complete CI/CD pipeline is automated using Jenkins and includes:

- GitHub source code management
- Automated testing using Pytest
- Static code analysis using SonarQube
- Docker image build
- Docker image push
- Amazon ECR integration
- Amazon EKS deployment
- Kubernetes rolling updates
- Health checks
- Horizontal Pod Autoscaling
- Prometheus monitoring
- Grafana dashboards
- Amazon RDS PostgreSQL
- AWS Secrets Manager
- EKS Pod Identity
- IAM based access control
- AWS Load Balancer

---

## 🏗️ Architecture

```text
                         Developer
                             |
                             v
                    +----------------+
                    |     GitHub     |
                    |  Source Code   |
                    +-------+--------+
                            |
                         Webhook
                            |
                            v
                    +----------------+
                    |     Jenkins    |
                    |     CI/CD      |
                    +-------+--------+
                            |
             +--------------+--------------+
             |              |              |
             v              v              v
        +---------+    +----------+   +-----------+
        |  Pytest |    | SonarQube |   |  Docker   |
        | Testing |    |  Analysis |   |   Build   |
        +---------+    +----------+   +-----+-----+
                                            |
                                            v
                                  +-------------------+
                                  |    Amazon ECR     |
                                  |  Docker Registry  |
                                  +---------+---------+
                                            |
                                            v
                                  +-------------------+
                                  |    Amazon EKS     |
                                  |    Kubernetes     |
                                  +---------+---------+
                                            |
                              +-------------+-------------+
                              |                           |
                              v                           v
                     +----------------+          +----------------+
                     | Flask Pod 1    |          | Flask Pod 2    |
                     | Replica        |          | Replica        |
                     +-------+--------+          +-------+--------+
                             |                           |
                             +-------------+-------------+
                                           |
                                           v
                                +----------------------+
                                | Amazon RDS PostgreSQL |
                                +----------------------+

                    AWS Secrets Manager
                            |
                            v
                     EKS Pod Identity
                            |
                            v
                           IAM

                    Monitoring Stack
                            |
                  +---------+---------+
                  |                   |
                  v                   v
             Prometheus            Grafana
                  |
                  v
          Kubernetes Metrics
🔄 CI/CD Pipeline
GitHub
   |
   v
Checkout
   |
   v
Pytest
   |
   v
SonarQube Analysis
   |
   v
Docker Build
   |
   v
Push Docker Image
   |
   v
Amazon ECR
   |
   v
Deploy to Amazon EKS
   |
   v
Kubernetes Rollout
   |
   v
Application Running
Jenkins Pipeline Stages
1. Checkout

Jenkins pulls the latest source code from the GitHub repository.

2. Test

Python dependencies are installed and automated tests are executed using Pytest.

The pipeline also performs Python syntax validation.

python -m pytest
python -m py_compile app.py
3. SonarQube Analysis

SonarQube is integrated into Jenkins for static code analysis and code quality checking.

4. Build Docker Image

The Flask application is packaged into a Docker container.

docker build -t <image>:<tag> .
5. Push Docker Image

The Docker image is pushed to Amazon ECR.

Jenkins
   |
   v
Docker Image
   |
   v
Amazon ECR
6. Deploy

Jenkins updates the Kubernetes Deployment with the new image and verifies the rollout.

kubectl set image deployment/devops-app ...
kubectl rollout status deployment/devops-app
🐍 Flask Application

The application is developed using Python Flask and provides REST API endpoints.

API Endpoints
Health Check
GET /health

Response:

Healthy
Employee API
GET /employees

Example response:

[
  {
    "id": 1,
    "name": "Vaibhav",
    "email": "vaibhav@example.com",
    "role": "DevOps Engineer"
  },
  {
    "id": 2,
    "name": "Rahul",
    "email": "rahul@example.com",
    "role": "Cloud Engineer"
  }
]
🐳 Docker

The Flask application is containerized using Docker.

Docker provides:

Consistent application environment
Application isolation
Portable deployments
Easy CI/CD integration
Versioned container images
☸️ Kubernetes

The application is deployed on Kubernetes using Amazon EKS.

Kubernetes resources used in the project:

Deployment
Service
Ingress
Horizontal Pod Autoscaler
Readiness Probe
Liveness Probe
PostgreSQL Deployment
Persistent Volume
Persistent Volume Claim
Kubernetes Secret
Application Replicas

The application runs with multiple replicas for availability.

              Kubernetes Service
                      |
           +----------+----------+
           |                     |
           v                     v
      Flask Pod 1           Flask Pod 2
☁️ AWS Infrastructure

AWS services used in the project:

AWS Service	Purpose
Amazon EKS	Kubernetes cluster
Amazon ECR	Docker image registry
Amazon RDS PostgreSQL	Managed PostgreSQL database
AWS Secrets Manager	Secure database credentials
IAM	Access control and permissions
EKS Pod Identity	AWS permissions for Kubernetes pods
Elastic Load Balancing	External application access
🔐 Security

Database credentials are not hardcoded in the application.

Credentials are securely stored in AWS Secrets Manager.

The application accesses them using EKS Pod Identity and IAM permissions.

Flask Application
       |
       v
EKS Pod Identity
       |
       v
IAM Permissions
       |
       v
AWS Secrets Manager
       |
       v
Database Credentials
       |
       v
Amazon RDS PostgreSQL

This prevents sensitive database credentials from being stored directly in application source code.

🗄️ PostgreSQL Database

PostgreSQL is used as the backend database.

Local Kubernetes Environment

During development, PostgreSQL can be deployed inside Kubernetes using:

PostgreSQL Deployment
PostgreSQL Service
Persistent Volume
Persistent Volume Claim
Kubernetes Secret
AWS Environment

For the production-style deployment, Amazon RDS PostgreSQL is used.

Amazon EKS
     |
     v
Flask Application
     |
     v
Amazon RDS PostgreSQL
📊 Monitoring and Observability

The project uses Prometheus and Grafana for Kubernetes monitoring and observability.

Monitoring Stack
Kubernetes Cluster
       |
       +-------------------+
       |                   |
       v                   v
   Prometheus           Metrics
       |
       v
    Grafana
       |
       v
   Dashboards

Monitoring components include:

Prometheus
Grafana
Alertmanager
Kubernetes metrics
Pod metrics
Node metrics
Kubernetes API metrics

Prometheus is configured to scrape available Kubernetes monitoring targets.

Grafana is used to visualize infrastructure and Kubernetes metrics through dashboards.

📈 Horizontal Pod Autoscaling

Horizontal Pod Autoscaler (HPA) is configured to automatically adjust application replicas based on resource utilization.

Low Traffic
    |
    v
2 Pods

High Traffic
    |
    v
More Pods

This improves scalability and resource utilization.

❤️ Health Probes

Kubernetes readiness and liveness probes are configured using the Flask /health endpoint.

Kubernetes
    |
    +--> Readiness Probe
    |
    +--> Liveness Probe
    |
    v
 /health
Readiness Probe

Checks whether the application is ready to receive traffic.

Liveness Probe

Checks whether the application is running correctly.

🔍 SonarQube

SonarQube is integrated into the Jenkins CI/CD pipeline.

It provides:

Static code analysis
Code quality checks
Issue detection
Maintainability analysis

Pipeline integration:

GitHub
   |
   v
Jenkins
   |
   v
Pytest
   |
   v
SonarQube
   |
   v
Docker Build
🧪 Automated Testing

Automated testing is implemented using Pytest.

Example successful test result:

collected 1 item

test_app.py . [100%]

1 passed

Tests are executed before Docker image creation and deployment.

This helps prevent failed or invalid builds from reaching the deployment stage.

📦 Amazon ECR

Amazon Elastic Container Registry is used to store Docker images.

Jenkins
   |
   v
Docker Build
   |
   v
Amazon ECR
   |
   v
Amazon EKS

The EKS deployment pulls the application image from Amazon ECR.

🌐 AWS Load Balancer

The Kubernetes Service is configured as a LoadBalancer to expose the Flask application externally.

Internet
    |
    v
AWS Load Balancer
    |
    v
Kubernetes Service
    |
    +-----------+
    |           |
    v           v
 Flask Pod 1  Flask Pod 2

The application can then be accessed through the AWS Load Balancer endpoint.

📁 Project Structure
flask-production-cicd/
│
├── aws/
│   └── README.md
│
├── k8s/
│   ├── deployment.yaml
│   ├── deployment-eks.yaml
│   ├── service.yaml
│   ├── service-eks.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml
│   ├── postgres-deployment.yaml
│   ├── postgres-service.yaml
│   ├── postgres-pvc.yaml
│   └── postgres-secret.yaml
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── sonar-project.properties
├── README.md
└── .gitignore
🛠️ Technology Stack
Application
Python
Flask
PostgreSQL
CI/CD
Git
GitHub
Jenkins
Pytest
SonarQube
Containers
Docker
Amazon ECR
Kubernetes
Kubernetes
Amazon EKS
Deployment
Services
Ingress
HPA
Readiness Probe
Liveness Probe
AWS
Amazon EKS
Amazon ECR
Amazon RDS PostgreSQL
AWS Secrets Manager
IAM
EKS Pod Identity
Elastic Load Balancer
Monitoring
Prometheus
Grafana
Alertmanager
Kubernetes Metrics
🎯 Key DevOps Concepts Demonstrated
CI/CD automation
Git-based development workflow
Jenkins pipeline automation
Automated testing
Static code analysis
Docker containerization
Docker image versioning
Amazon ECR
Kubernetes deployment
Amazon EKS
Rolling updates
Health checks
Horizontal Pod Autoscaling
AWS cloud deployment
Amazon RDS
Secrets management
IAM based access control
EKS Pod Identity
Prometheus monitoring
Grafana dashboards
Application observability
Kubernetes troubleshooting
🚀 Deployment Result

The application is successfully deployed on Amazon EKS with:

2 Flask application replicas
Amazon ECR container image
Amazon RDS PostgreSQL backend
AWS Load Balancer
AWS Secrets Manager integration
EKS Pod Identity
IAM permissions
Kubernetes health probes
Horizontal Pod Autoscaling
Prometheus monitoring
Grafana visualization
Jenkins automated CI/CD

Application endpoints:

/health
/employees

Example:

curl http://<AWS-LOAD-BALANCER>/health
Healthy
curl http://<AWS-LOAD-BALANCER>/employees
📸 Project Screenshots

Screenshots can be added to this section to demonstrate the implementation.

Recommended screenshots:

Jenkins successful CI/CD pipeline
Pytest successful execution
SonarQube analysis
Amazon EKS cluster
Kubernetes pods and services
Amazon ECR repository
Prometheus Target Health
Grafana dashboard
AWS Load Balancer application response
/health and /employees API responses
👨‍💻 Author

Vaibhav Surase

DevOps / Cloud Engineer

GitHub: https://github.com/vaibhav-surase
