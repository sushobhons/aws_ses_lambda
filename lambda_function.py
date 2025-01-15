import json
import boto3

# Initialize the SES client
ses_client = boto3.client('ses')
source_email = 'source@example.com'
template_name = 'Template1'  # Name of the SES email template

def fetch_user_emails():
    # Example hardcoded emails (replace with dynamic fetching logic)
    return [
        "user1@example.com",
        "user2@example.com",
        "user3@example.com"
    ]
    
# Helper function to send templated emails to a chunk of recipients
def send_templated_email_chunk(recipients):
    try:
        response = ses_client.send_bulk_templated_email(
            Source=source_email,
            Template=template_name,
            DefaultTemplateData=json.dumps({}),  # Default template data (empty as no personalization required)
            Destinations=[
                {
                    'Destination': {
                        'ToAddresses': [recipient]
                    }
                }
                for recipient in recipients
            ]
        )
        print(f"Templated email sent to: {recipients}")
        return response
    except Exception as e:
        print(f"Failed to send templated email to {recipients}. Error: {str(e)}")
        return None

def lambda_handler(event, context):
    # Fetch all user emails dynamically
    all_recipients = event.get('recipients', fetch_user_emails())
    
    # Chunk recipients into groups of 50
    chunk_size = 50
    recipient_chunks = [all_recipients[i:i + chunk_size] for i in range(0, len(all_recipients), chunk_size)]
    
    # Send templated emails in chunks
    for chunk in recipient_chunks:
        send_templated_email_chunk(chunk)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Templated emails sent successfully!')
    }
