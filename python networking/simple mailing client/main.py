import smtplib, ssl # to send emails from smpt protocol
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("The body of the email is here")
msg['Subject'] = 'testing mail code'
msg['From'] = '@gmail.com' # your email here
msg['To'] = '@gmail.com' # email to send to here

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], '') # put password for email in from
    smtp.send_message(msg)
