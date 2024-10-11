import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_mail(subject,body,to_mail):
    
    from_mail=os.getenv("usermail_id")
    password=os.getenv("password")
    
    msg=MIMEMultipart()
    msg["From"]=from_mail
    msg["To"]=to_mail
    msg["Subject"]=subject
    msg.attach(MIMEMultipart(body,"plain"))
    
    try:
        # Connect to the server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_mail, password)
        text = msg.as_string()
        server.sendmail(from_mail, to_mail, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    
    

subject="test email"
body="this is the test email sent from python"
to_mail="lokkshanaasivaraman@gmail.com"

send_mail(subject,body,to_mail)