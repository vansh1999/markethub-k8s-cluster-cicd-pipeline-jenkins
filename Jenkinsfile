pipeline {

    environment {
        dockerimagename = "vansh1999/markethub"
        dockerImage = ""
    }

    agent any

    stages {

        stage("Checkout Source") {
            steps {
                git branch: 'main', url: 'https://github.com/vansh1999/markethub-k8s-cluster-cicd-pipeline-jenkins.git'
            }
        }

        stage("Code Test") {
            steps {
                echo "Code test successful"
            }
        }

        stage("Build Image") {
            steps {
                script {
                    dockerImage = docker.build(dockerimagename)
                }
            }
        }

        stage("Pushing Image to DockerHub") {

            environment {
                registryCredential = 'dockerhublogin'
            }

            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
                        dockerImage.push("latest")
                    }
                }
            }
        }

        stage("Deploy app to Kubernetes") {
            steps {
                script {
                    kubernetesDeploy(configs: "deployment.yml", kubeconfigId: "kubernetes")
                }
            }
        }
    }

    post {
        always {
            echo "========END========"
        }
        success {
            echo "========Pipeline executed successfully========"
        }
        failure {
            echo "========Pipeline execution failed========"
        }
    }
}

