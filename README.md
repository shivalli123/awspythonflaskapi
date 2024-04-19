## Serverless Application Setup
This repository contains a simple serverless application built using AWS Lambda and API Gateway. The application is written in Python and utilizes the Serverless Framework for deployment.

## Overview
The serverless.yml file is used to define the configuration and resources for deploying a serverless application on AWS Lambda using the Serverless Framework.

## Steps for Deployment
- Install the Serverless Framework globally on your local machine using npm:
 npm install -g serverless

-Update the serverless.yml file with your application-specific settings, such as function handler, runtime, and events.
- Deploy the serverless application to AWS Lambda by running the following command:
  serverless deploy
-Test the deployed application by invoking the Lambda function directly or accessing the API Gateway endpoint provided in the deployment output.

## Files
1. serverless.yml: This file contains the configuration for deploying the serverless application. It defines the AWS Lambda function, API Gateway endpoint, and other necessary resources.
2. lambdahandler.py: This file contains the Python code for the AWS Lambda function. It defines the lambda_handler function, which serves as the entry point for the Lambda function.

## Using Layers to Add Libraries
If you need to include additional libraries or dependencies in your Lambda function, you can use Lambda layers. Here's how to add libraries using layers:

- Create a Layer: Create a new directory for your layer and include the necessary libraries. For example, to add the requests library, create a directory named python and install the library using pip:
mkdir python
pip install flask -t python/
pip install requests -t python/

- Package the Layer: Package the contents of the layer directory into a ZIP file:
cd python
zip -r layer.zip .

- Deploy the Layer: Upload the ZIP file to AWS Lambda as a layer. You can do this using the AWS Management Console or the AWS CLI.
- Attach the Layer to Lambda Function: In the serverless.yml file, specify the ARN of the layer to attach it to the Lambda function. Use the layers property under the function's configuration.
With these steps, you can easily include additional libraries in your Lambda function using layers.


## Usage
-Dependencies: Ensure that the required dependencies such as Flask, requests, and awsgi are installed in your development environment.
-Configuration: Update the Flask application code in lambdahandler.py with your application-specific logic and routes.
-Testing: Test the Flask application locally using the Flask development server. Run the Flask application with the command:
          flask run
-Deployment: Deploy the Flask application as a serverless function on AWS Lambda using the Serverless Framework.
