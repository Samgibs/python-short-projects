from email.message import EmailMessage
import smtplib
import ssl

emailsender="captainsamuelqs@gmail.com"
emailpassword="yoay gxky evde eyym"
emailreceiver="mukabi339@gmail.com"

subject="revising"
body="""The function then returns a tuple with the sum of corresponding elements from"""

em=EmailMessage()
em["from"]=emailsender
em["To"]=emailreceiver
em["subject"]=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(emailsender,emailpassword)
    smtp.sendmail(emailsender,emailreceiver,em.as_string())