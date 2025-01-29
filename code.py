from sys import *
import os
import time
import urllib.request
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout = 5)
        return True
    except urllib.request.URLError as err:
        return False
    
def MailSender(time):
    try:
        fromaddr = "chakuli250@gmail.com"
        toaddr = "shreyapattewar3105@gmail.com"
        
        msg = MIMEMultipart()
        
        msg['From'] = fromaddr
        
        msg['To'] = toaddr
        
        body = """
        Hello %s
        Good Morning..
        Have a very Wonderful Day!!
        
        Thanks & Regards
        Yours...
        
        This is auto generated mail.
        Do not reply!!!
        """ %(toaddr)
    
        Subject = """
        Have a nice day : %s
        """ %(time)
        
        msg['Subject'] = Subject
        
        msg.attach(MIMEText(body,'plain'))
      
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        s.starttls()
        
        s.login(fromaddr, "enip nzzl mmpk jtwz")
        
        text = msg.as_string()
        
        s.sendmail(fromaddr, toaddr, text)
        
        s.quit()
        
        print("Mail has been sent succesfully...\n")

                
    except Exception as E:
        print("Unable to send mail.", E)
        
def finalBlock():
    
    connected = is_connected()
    
    if connected:
        startTime = time.time()
        MailSender(time.ctime())
        endTime = time.time()
        
    else:
        print("There is no internet connection")
        
        
def main():
    finalBlock()
    
if __name__=="__main__":
    main()
