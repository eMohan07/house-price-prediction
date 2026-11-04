pipeline {
    agent any

    environment {
        APP_NAME     = "house-price-predictor"
        APP_PORT     = "8501"
        IMAGE_NAME   = "house-price-predictor"
        IMAGE_TAG    = "${BUILD_NUMBER}"
        HEALTH_URL   = "http://localhost:8501/_stcore/health"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Stage 1: Checking out source code..."
                checkout scm
            }
        }

        stage('Dependency installation') {
            steps {
                echo "Stage 2: Installing project and CI dependencies..."
                script {
                    if (isUnix()) {
                        sh 'python3 -m pip install --upgrade pip'
                        sh 'pip install -r requirements.txt pytest flake8'
                    } else {
                        bat 'python -m pip install --upgrade pip'
                        bat 'python -m pip install -r requirements.txt pytest flake8'
                    }
                }
            }
        }

        stage('Code validation') {
            steps {
                echo "Stage 3: Validating syntax and code structure..."
                script {
                    if (isUnix()) {
                        sh 'python3 -m py_compile app.py src/*.py tests/*.py'
                        sh 'flake8 src tests app.py --count --select=E9,F63,F7,F82 --show-source --statistics || true'
                    } else {
                        bat 'python -m py_compile app.py src/constants.py src/predict.py src/train.py src/utils.py tests/test_prediction.py'
                        bat 'python -m flake8 src tests app.py --count --select=E9,F63,F7,F82 --show-source --statistics || ver>nul'
                    }
                }
            }
        }

        stage('Automated tests') {
            steps {
                echo "Stage 4: Executing automated test suite..."
                script {
                    if (isUnix()) {
                        sh 'pytest tests/ -v'
                    } else {
                        bat 'python -m pytest tests/ -v'
                    }
                }
            }
        }

        stage('Docker image build') {
            steps {
                echo "Stage 5: Building Docker container image..."
                script {
                    if (isUnix()) {
                        sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
                    } else {
                        bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
                    }
                }
            }
        }

        stage('Deployment through Ansible') {
            steps {
                echo "Stage 6: Deploying container via Ansible playbook..."
                script {
                    if (isUnix()) {
                        sh 'ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --extra-vars "image_tag=latest"'
                    } else {
                        // On Windows nodes with native or WSL Ansible:
                        bat '''
                            where ansible-playbook >nul 2>nul && (
                                ansible-playbook -i ansible/inventory.ini ansible/deploy.yml --extra-vars "image_tag=latest"
                            ) || (
                                echo Native ansible-playbook not detected on Windows host. Running container deployment fallback... &&
                                docker rm -f house-price-predictor 2>nul || ver>nul &&
                                docker run -d --name house-price-predictor -p 8501:8501 --restart unless-stopped house-price-predictor:latest
                            )
                        '''
                    }
                }
            }
        }

        stage('Health verification') {
            steps {
                echo "Stage 7: Verifying application health endpoint..."
                script {
                    if (isUnix()) {
                        sh '''
                            for i in {1..12}; do
                                if curl -s -f http://localhost:8501/_stcore/health; then
                                    echo "Application is Healthy and reachable!"
                                    exit 0
                                fi
                                echo "Awaiting application initialization... ($i/12)"
                                sleep 5
                            done
                            echo "Application health check timed out!"
                            exit 1
                        '''
                    } else {
                        bat '''
                            powershell -Command "for ($i = 1; $i -le 12; $i++) { try { $response = Invoke-RestMethod -Uri 'http://localhost:8501/_stcore/health' -TimeoutSec 3; if ($response -eq 'ok') { Write-Host 'Application is Healthy and reachable!'; exit 0 } } catch { Write-Host ('Awaiting application initialization... (' + $i + '/12)'); Start-Sleep -Seconds 5 } }; Write-Error 'Application health check timed out!'; exit 1"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline run completed."
        }
        success {
            echo "CI/CD Pipeline succeeded: House Price Predictor deployed and healthy at http://localhost:8501"
        }
        failure {
            echo "Pipeline execution failed. Review stage logs above."
        }
    }
}
