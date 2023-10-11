from email.message import EmailMessage
import smtplib
import ssl

emailsender="captainsamuelqs@gmail.com"
emailreciever="samuelgibson722@gmail.com"
emailpassword="yoay gxky evde eyym"

subject="learning python"
body="""created an email sender using python"""

em=EmailMessage()
em["from"]=emailsender
em["To"]=emailreciever
em["subject"]=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(emailsender,emailpassword)
    smtp.sendmail(emailsender,emailreciever,em.as_string())