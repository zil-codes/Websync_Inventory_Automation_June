pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
        PATH = "/Users/zillurrahman/Library/Python/3.9/bin:/usr/local/bin:/usr/bin:/bin:${PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/zil-codes/Websync_Inventory_Automation_June.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                    pip3 install allure-pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    python3 -m pytest tests/ \
                        --alluredir=allure-results \
                        -v \
                        --tb=short
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Tests failed! Check Allure report.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
