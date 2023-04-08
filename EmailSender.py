from email.message import EmailMessage
import ssl
import smtplib

email_sender = '' #your email ID
email_password = '' #generated app password from gmail or import from Environmental varibale

email_receiver = '' #perons or group of pepole sent this email to use , to seprate emails 

subject = '' #Subject of the mail aka Email Title 

body = """ """ #message here

#dont change anything below here 
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())



