import smtplib

def send_mail(recv,data,pw):
    sender="helloabhilash2000@gmail.com"
    receiver=recv
    password=pw
    message=data
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,message) 
