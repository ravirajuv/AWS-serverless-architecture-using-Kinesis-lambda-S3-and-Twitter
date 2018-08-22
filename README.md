# AWS-serverless-architecture-using-Kinesis-lambda-S3-and-Twitter

# To do this yourself you will need the below resources:
•	An active AWS account with kinesis firehose delivery stream, lambda function and S3.
•	Twitter developer account with an app created in it.
•	Keys and Tokens of the app created.

# Steps to follow:
• To create a firehose delivery stream go to services>>Analytics>>Kinesis>>DataFirehos>>CreateDeliveryStream(while creating firehose you need to provide a S3 location to store the data).
• In this repository I have included a zip file(twitter_data.zip) to upload it to your lambda function which includes all the required python packages and their dependencies. 
•	After uploading the zip file into your lambda function console you can edit the code inline and provide required details.
•	Don't forget to attach required policies to your aws role which will be used to execute your lambda function and update the handler to twitter_data.lambda_handler to avoid import error.

# Knowledge Resources:
To create twitter developer app >> https://developer.twitter.com
To create a custom aws role >> https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html
To create a aws firehose delivery stream >> https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html
To create a aws lambda function >> https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-create-function.html







