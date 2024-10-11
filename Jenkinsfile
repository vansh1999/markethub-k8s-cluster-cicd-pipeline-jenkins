pipeline {
    
    agent { label 'jenkins-agent' }
    
    stages{
        
        stage("Code"){
            steps{
                git url: 'https://github.com/vansh1999/markethub.git' , branch: 'main' 
                echo "Code received successfully from github +++"
                
            }
        }
        
        stage("Build and Test"){
            steps{
                sh 'docker build . -t markethub'
            }
        }
        
    //     stage("login in dockerhub"){
	//          steps{
    //              withCredentials([usernamePassword(credentialsID: 'markethub-pass' , passwordVariable: 'dockerHubPassword' , usernameVariable: 'dockerHubUsername' )]){
	// 	                sh 'docker login -u ${env.dockerHubUsername} -p ${dockerHubPassword}''
    //                      }
    //             }
    //     }
        
        stage("Deploy"){
            steps{
                sh 'docker run -d -p 8000:8000 markethub:latest'
            }
        }
        
        
    }
    
    
}
