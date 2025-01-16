# AWS SES Bulk Templated Email Sender using LAMBDA

This repository contains a Lambda function for sending bulk templated emails using AWS Simple Email Service (SES). It splits recipient email addresses into manageable chunks and sends emails in batches using SES's bulk email feature.

## Features

- Dynamically fetch recipient email addresses or accept them via event payload.
- Chunk email addresses into groups of 50 (SES limit).
- Send bulk templated emails using AWS SES.
- Basic error handling and logging.

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
5. Give the role a name (e.g., `SESLambdaRole`) and click **Create Role**.

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

---
