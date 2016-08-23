import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
from_email = Email("azimshaik91@gmail.com")
subject = "Hello World from the SendGrid Python Library!"
to_email = Email("ashaik1@kent.edu")
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
