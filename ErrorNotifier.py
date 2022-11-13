import smtplib
from email.message import EmailMessage

# variables
smtp_server = "smtp.gmail.com"
sender_email = "celeste.valambhia@gmail.com"
receiver_email = "celeste.valambhia@gmail.com"
port = 587
message = "Hi,\n\nError occured in IoT. Please find attached logs for more information.\n\nRegards,\nCeleste"
subject = "IoTLogiqConnectiv Failure Logs"

def SendEmail(log):
    email_message = EmailMessage()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject
    email_message.set_content(message)

    filename = "./Logs/IoTLogs.log"
    email_message.add_attachment(open(filename, "r").read(), filename="IoTLogs.log")

    # creates SMTP session
    s = smtplib.SMTP(smtp_server, port)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_email, password)

    # sending the mail
    s.send_message(email_message)
    s.quit()

    print("Email Sent to Administrator")