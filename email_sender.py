import  smtplib
try:
    server=smtplib.SMTP("smtp.gmail.com",port=587)
    #serverkostart
    server.starttls()
    
    #receiver mail credentials
    receiver_mail=input("enter the reciver mail")
    sender_email="akashpandit9997@gmail.com"
    password="aaep kkiu lwku vavk"

    #login
    server.login(sender_email,password=password)
    subject=input("enter the subject:- ")
    body=input("enter the body here:- ")
    message=f"Subject:{subject} \n \n {body}"
    server.sendmail(sender_email,receiver_mail,message)
    print("mail sent successfully")
except Exception as e:
    print(e)
    
    