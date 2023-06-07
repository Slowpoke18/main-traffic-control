import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configurations
sender_email = 'senderemail'
sender_password = 'senderpassword'
receiver_email = 'rishivs2308@gmail.com'
subject = 'Test Email'
message = 'This is a test email sent from Python.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the MIMEMultipart object
msg.attach(MIMEText(message, 'plain'))

# SMTP server configurations (Gmail example)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Establish a secure connection with the SMTP server
smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()

# Login to the email account
smtp_connection.login(sender_email, sender_password)

# Send the email
smtp_connection.sendmail(sender_email, receiver_email, msg.as_string())

# Close the SMTP connection
smtp_connection.quit()

print("Email sent successfully.")
