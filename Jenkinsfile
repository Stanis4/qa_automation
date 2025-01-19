


pipeline{
    agent{
        label 'windows'
    }

    options{
        timeout(time: 1, unit:'HOURS')
        retry(2)
    }

    parameters{
        string(name: 'run_command', defaultValue: 'python -m pytest tests\\form_test.py', description: 'Run autotests suite')
        choice(name: 'Test choice', choices: ['1', '2', '3'], description: 'Test choice params')
    }

    triggers{
        cron('@midnight')
    }

    environment{
        PLATFORM = 'CHROME'
        BROWSER_VERSION = 132
        ENV_FILE = credentials(config_file.toString())
    }

    stages{

        stage('Checkout'){
            steps{
                git branch: 'main', credentialsId: 'github_credentials_with_password', url: 'https://github.com/Stanis4/qa_automation.git'
            }
        }

        stage('Create venv'){
            steps{
                script{
                    sh '''
                        python -m venv %WORKSPACE%\\venv
                        call %WORKSPACE%\\venv\\Scripts\\activate.bat
                        pip install -r requirements.txt
                        '''
                }
            }
        }

        stage('Run test suite'){
            steps{
                script{
                    sh '''
                    call %WORKSPACE%\\venv\\Scripts\\activate.bat
                    %run_command%
                    '''
                }
            }
            post {
                always {
                    allure includeProperties: false,
                     jdk: '',
                     results: [[path: '/allure-results']]
                }
            }
        }
    }
    post {
        always{
            script{
                cleanWs()
                sh 'echo WORKSPACE was deleted'
            }
        }
    }
}