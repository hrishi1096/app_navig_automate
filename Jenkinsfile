pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                           branches: [[name: '*/develop']],
                           extensions: [],
                           userRemoteConfigs: [[credentialsId: 'hrishib_github_credentials',
                                                url: 'git@github.com:hrishi1096/app_navig_automate.git']]
                        ])
            }
        }
        stage('Build') {
            steps {
                git branch: 'develop',
                credentialsId: 'hrishib_github_credentials',
                url: 'git@github.com:hrishi1096/app_navig_automate.git'

                browserstack('hrishib_browserstack_credentials') {
                    sh '''python3 -m pip install -r requirements.txt
                          python3 -m pytest -n 5 auto_app_navigate.py'''
                }
            }
        }
        stage('Test') {
            steps {
                echo "This job has been tested"
            }
        }
    }
}
