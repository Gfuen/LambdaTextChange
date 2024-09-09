# LambdaTextChange

The following is an AWS Lambda Function project that uses an S3 Object Creation event trigger on an S3 Test Bucket
and determines if the uploaded object is a text file. If the uploaded object is a text file then the AWS Lambda function
downloads the file and replaces the text "Hello World" with "Goodbye World" and then replaces that same S3 Object
within the S3 Bucket.
