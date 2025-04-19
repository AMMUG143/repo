pipeline{
    agent any
    stages{
        stage("git clone"){
            steps{

                git credentilasId: 'AMMU', urL:"https://github.com/AMMUG143/first.git", branch: 'main'

            }
        }
        stage('install dependencies'){
            steps{
                bat '''
                C:\\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install pytest
                '''

            }
        }
        stage("testing"){
            steps{
                bat '''
                    venv\\Scripts\\activate
                    pytest test.py
                '''
            }
        }
        stage("deploy"){
            steps{
                bat '''
                venv\\Scripts\\activate
                C:\\Users\\amrutha\\AppData\\Local\\Programs\\Python\\Python313\\python.exe helo.py
                '''
                
                
            }
        }
    }
}