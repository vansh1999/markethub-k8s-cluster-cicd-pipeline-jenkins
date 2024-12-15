# MarketHub CI/CD Pipeline: Deploy Django Application to Kubernetes Using Jenkins

This repository demonstrates a complete CI/CD pipeline for deploying a Django application to a Kubernetes cluster using Jenkins. It automates the workflow of building, testing, containerizing, and deploying a Django app seamlessly.

## Overview

The goal of this project is to automate the following tasks:

Code Testing: Ensure the app functions as expected.

Docker Image Creation: Containerize the Django app.

Pushing to Docker Hub: Push the Docker image to Docker Hub.

Kubernetes Deployment: Deploy the app to a Kubernetes cluster.


## Architecture

The workflow for the CI/CD pipeline is as follows:

A developer commits code to the GitHub repository.

Jenkins triggers a pipeline to:

Run tests.

Build a Docker image.

Push the image to Docker Hub.

Deploy the app to Kubernetes.

The Kubernetes cluster hosts the Django application.

CI/CD Workflow Diagram

![pipeline-diagram](https://github.com/user-attachments/assets/33290bcc-79c8-4ace-af17-dee3587f244c)

## Technologies Used

Jenkins: For setting up the CI/CD pipeline.

Docker: To containerize the Django application.

Kubernetes: For application deployment and orchestration.

AWS EC2: Host Jenkins and Kubernetes clusters.

GitHub: Source code version control.

Python 3.9: For the Django application.

## Pipeline Stages

Below are the Jenkins pipeline stages configured in the Jenkinsfile:

Checkout Source: Pulls code from GitHub.

Code Test: Verifies code integrity (placeholder for Django tests).

Build Image: Builds a Docker image using the Dockerfile.

Push to DockerHub: Pushes the built image to Docker Hub.

Deploy to Kubernetes: Deploys the app using Kubernetes manifest files (deployment.yml).

![Screenshot 2024-12-14 at 3 01 49 AM](https://github.com/user-attachments/assets/7177e415-4e55-4614-ba1b-9b3dfd316438)

## Blog 

https://medium.com/@vansh.bhardwaj1999/django-application-markethub-ci-cd-pipeline-to-deploy-on-kubernetes-cluster-using-jenkins-f17396d9182f

## Author

Vansh Bhardwaj

Feel free to fork, clone, and contribute to this repository! 🚀








