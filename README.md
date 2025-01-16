# AWS SES Bulk Templated Email Sender using LAMBDA

This repository contains a Lambda function for sending bulk templated emails using AWS Simple Email Service (SES). It splits recipient email addresses into manageable chunks and sends emails in batches using SES's bulk email feature.

## Features

- Dynamically fetch recipient email addresses or accept them via event payload.
- Chunk email addresses into groups of 50 (SES limit).
- Send bulk templated emails using AWS SES.
- Basic error handling and logging.
- Support for fetching email addresses from an S3 Excel file (XLSX format).

## Prerequisites

### AWS SES Setup

#### Create SES Identity:

1. Go to the [SES Console](https://console.aws.amazon.com/ses/).
2. Click on **Create Identity** and choose "Email address" for the **Identity Type**.
3. Enter your source email address (e.g., `source@example.com`) and click on **Create Identity**.
4. Verify your email address by checking your inbox and clicking the verification link.

#### Create an SES Template:

1. Create an email template named `Template1` in SES.

   Example JSON template:
   
   ```json
   {
     "TemplateName": "Template1",
     "SubjectPart": "Your Subject Here",
     "TextPart": "Hello {{name}},\nThis is a test email.",
     "HtmlPart": "<h1>Hello {{name}}</h1><p>This is a test email.</p>"
   }
   ```

### AWS IAM Role Setup

#### Create an IAM Role:

1. Go to the [IAM Console](https://console.aws.amazon.com/iam/).
2. Click on **Roles** in the left menu and then **Create Role**.
3. Select **Lambda** as the use case and click **Next**.
4. Search for and attach the policy **AmazonSESFullAccess**.
5. Attach the AmazonS3ReadOnlyAccess policy to allow Lambda to read objects from your S3 bucket.
6. Give the role a name (e.g., `SESLambdaRole`) and click **Create Role**.

### AWS Lambda Setup

#### Create a Lambda Function:

1. Go to the [Lambda Console](https://console.aws.amazon.com/lambda/).
2. Click **Create Function** and provide a name for your function (e.g., `SESBulkEmailSender`).
3. Select **Python 3.x** as the runtime.
4. For the **Execution Role**, choose the IAM role you created (e.g., `SESLambdaRole`).

#### Configure Environment Variables (Optional):

- `SOURCE_EMAIL`: The source email address.
- `TEMPLATE_NAME`: The SES template name.   

#### Deploy the Code:

1. Copy-paste the Python code into the Lambda function's code editor.
2. Click on the **Deploy** button and wait for deployment notification.

#### Test the Lambda Function:

1. Click on the **Test** button, give your test event a name, and provide the sample event payload (see below).
2. Click **Save** and then **Test** again to trigger the Lambda function.
3. Check your inbox to verify that the email has been sent successfully.

#### Fetching Emails from S3:

This Lambda function can fetch recipient emails from an Excel file stored in an S3 bucket. The S3_BUCKET_NAME and S3_FILE_KEY environment variables need to be set to point to your S3 bucket and file.

The file should be in XLSX format and contain a column of email addresses. The Lambda function reads the emails from this file and sends the templated email to each address.

The Lambda function reads the emails from this file and sends the templated email to each one.
#### Steps to Fix Panda Issue:
Use Lambda Layers:

1. In the Lambda console, navigate to your function.
2. Under the "Layers" section, click "Add a layer."
3. Choose a layer either from your own layers or from the available Lambda layers in the AWS marketplace.

#### Steps to Fix the Timeout Issue:
Increase Lambda Timeout:

1. Go to the AWS Lambda Console.
2. Find and select your Lambda function.
3. Under the Configuration tab, click on General configuration.
4. Increase the timeout setting to a higher value (e.g., 10 or 15 seconds, depending on how long the operation takes).
5. Click Save.

---
