#python3 only
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

destination_email=input("\nWhat email address would you like to send a message to?\n>")
email_subject=input("\nDefine the subject.\n>")
email_content=input("\nWhat would you like in the body of the email?\n>")

message = Mail(
    from_email= os.environ.get("my_email"),
    to_emails= destination_email,
    subject= email_subject,
    html_content= email_content)
try:
    sg = SendGridAPIClient(os.environ.get('sendgrid_key'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    print("\nEmail Sent")
except Exception as e:
	print(f"{e}, Unable to send.\nEnsure you input the variables correctly and try again.")
	#IDE always states SyntaxError: invalid syntax when using F strings. works regardless
