import smtplib
from email.message import EmailMessage
import ssl
# list of email_id to send the mail
sender = "lazydev3@gmail.com"
receiver = "mohitmah50@gmail.com"
password = "vftt qjyt gyvo owcu"

subject = "Test Successful"
body = "Go celebrate!"

em = EmailMessage()
em['From'] = sender
em['To'] = receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, em.as_string())