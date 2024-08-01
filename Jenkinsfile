pipeline {
    agent {
      docker {
        image 'python:3'
      }
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git branch: 'main', url:'https://github.com/krishachetan89/get_ip_address.git'
            }
        }
        stage('Run ls') {
            steps {
                // Run the ls command to check files
                sh 'ls'
            }
        }

        stage('Run ip_print with input1.json') {
            steps {
                // Run the ip_print.py script with input1.json
                sh 'python3 ip_print.py input1.json'
            }
        }

        stage('Run ip_print with input2.json') {
            steps {
                // Run the ip_print.py script with input2.json
                sh 'python3 ip_print.py input2.json'
            }
        }
    }
}
