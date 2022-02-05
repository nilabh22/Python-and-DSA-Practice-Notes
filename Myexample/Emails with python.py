import smtplib
connect_to_gmail = smtplib.SMTP('smtp.gmail.com',port=587)
connect_to_gmail.ehlo() # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
connect_to_gmail.starttls() #StartTLS is a protocol command used to inform the email server that the email client wants to upgrade from an insecure connection to a secure one using TLS
#input("What is your password?:") # But by this anyone having your python script can see your password
# SO we use getpass library specially designed for this
import getpass
#password = getpass.getpass("Enter Password: ") # it will hide the characters and length too
email = input("Email: ")
password = input("password: ")
connect_to_gmail.login(email,password)
print("It is connected!!") # It wont give any hint thats why i printed the "it is connected"
from_address = email
to_address = input("reciever_mail: ")
message_subject = input("Enter your mail Subject Here: ")
message_body = input("Enter your msg here: ")
msg = "Subject: "+message_subject +'\n'+message_body
connect_to_gmail.sendmail(from_address, to_address, msg)