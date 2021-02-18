node()
{
    print "DEBUG: parameter foo = ${name}"
    print "DEBUG: parameter version = ${version}"
    print "DEBUG: parameter location = ${source}"
    print "DEBUG: parameter GOOGLE_SERVICE_ACCOUNT_KEY ${GOOGLE_SERVICE_ACCOUNT_KEY}"
    print "DEBUG: parameter GOOGLE_PROJECT_ID ${GOOGLE_PROJECT_ID}"


}
pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                print "DEBUG: parameter build "
            }
        }
        stage('Test') { 
            steps {
                // 
		  print "DEBUG: parameter test "

            }
        }
        stage('Deploy') { 
            steps {
		    print "DEBUG: parameter deploy "

                	//Deploy to GCP
				sh """
					#!/bin/bash 
					echo "deploy stage";
					curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-225.0.0-linux-x86_64.tar.gz;
					echo "-----------------------------------------";
					tar -xvf /tmp/google-cloud-sdk.tar.gz -C /tmp/;
					echo "-----------------------------------------";
					/tmp/google-cloud-sdk/install.sh -q;
					echo "-----------------------------------------";
                   			source /tmp/google-cloud-sdk/path.bash.inc;
					echo "-----------------------------------------";
					
					 gcloud config set project ${GOOGLE_PROJECT_ID};
					 gcloud auth activate-service-account --key-file ${GOOGLE_SERVICE_ACCOUNT_KEY};
					 
					 gcloud config list;
					 gcloud app deploy --version=v01;
                    echo "Deployed to GCP"
				"""
			}
            }
        }
    
}
