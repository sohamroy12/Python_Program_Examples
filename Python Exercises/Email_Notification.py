import smtplib
import sys
from email.message import EmailMessage

email_address = sys.argv[1]
email_password = sys.argv[2]
to_addrs = sys.argv[3]
to_addrs1 = sys.argv[4]
print(email_address, email_password, to_addrs, to_addrs1)

# Send email from a function.
def send_email():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(email_address, email_password )
        connection.sendmail(from_addr=email_address, to_addrs=to_addrs,
        msg="subject:Sent fron PyCharm IDE \n\n This is my test message from python Code. Secured the email this time")

# send_email()

# Send email from outside function
connection1 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
connection1.login(email_address, email_password)
connection1.sendmail(from_addr=email_address, to_addrs=to_addrs1, msg="subject:Sent fron PyCharm IDE \n\n This is my test message from python Code. Secured the email this time")
connection1.close()
