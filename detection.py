#!/usr/bin/env python3

#---------------------------------------------------------#
#  Copy Right to ~> ajdev05                               #
#  Follow Me on Github ~> https://github.com/ajdev05/     #
#---------------------------------------------------------#

import subprocess
import os
import time 
import requests
import smtplib, ssl
from email.message import * 

os.system("clear")
dis_webhook="" # Your Discord webhook
maxmbps=10000 #is packets go over this number the process initiates 
while True:
    email1_rec=[""] # put the recivers Eamil Address
    interface = "ens18" # Your Interface name
    pko = int(subprocess.check_output("grep "+interface+": /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'",shell=True))
    time.sleep(1)
    pkn = int(subprocess.check_output("grep "+interface+": /proc/net/dev | cut -d :  -f2 | awk '{ print $2 }'",shell=True))
    os.system("clear")
    pk = pkn - pko
    ttl_pk=pk
    print(ttl_pk," Packets")

    ## Conversions
    packets_dis =  str(f"Packets: {ttl_pk}")
    mbps_con = int(ttl_pk * 8 * 2 * 1518) / 1000000
    mbps_dis=str(f"Mbps: {mbps_con}")
    sip = "" # Enter your Servers IP Address
    x = f"""**```

!ATTACK DECETED!

! Server Under Attack !

Server IP: {sip}

Server Location: your server location 

Server Hostname: your server hostname

Server Name: your server name

{packets_dis}        

{mbps_dis}     

    ```**"""
    def att_email():
        # Your email credentials
        
        email_send = "your_email@gmail.com"
        email_passwd = "your password"

        subject = "Attack Detected on Server"

        body=f"""
!ATTACK DECETED!

! Server Under Attack !

Your message here

ATTACK STATS:

Server IP: {sip}

Server Location: your server location 

Server Hostname: your server hostname

Server Name: your server name

{packets_dis}        

{mbps_dis}
        """

        em = EmailMessage()
        em["From"] = email_send
        em["to"] = email1_rec
        em["Subject"] = subject
        em.set_content(body)

        context=ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_send,email_passwd)
            smtp.sendmail(email_send,email1_rec,em.as_string())
    
    ###################### End ###############################
    def end_email():
        email_send = "your_email@gmail.com"
        email_passwd = "your password"
        

        subject1 = "Attack No Longer Detected On Server"

        body1=f"""

! ATTACK NO LONGER DETECTED ON THE NETWORK !

your message here

ATTACK STATS:

Server IP: {sip}

Server Location: your server location 

Server Hostname: your server hostname

Server Name: your server name

{packets_dis}        

{mbps_dis}
        """

        em1 = EmailMessage()
        em1["From"] = email1_send
        em1["to"] = email1_rec
        em1["Subject"] = subject1
        em1.set_content(body1)

        context1=ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context1) as smtp:
            smtp.login(email1_send,email1_passwd)
            smtp.sendmail(email1_send,email1_rec,em1.as_string())
##############################################################################

    if pk > maxmbps:
        print("Detected")
        rep = requests.post(dis_webhook, data={"content":x})
        att_email()
        time.sleep(300)
        end_att=f"""
        **```
!ATTACK DECETED!

! End of Attack !

Server IP: {sip}

Server Location: your server location 

Server Hostname: your server hostname

Server Name: your server name

{packets_dis}        

{mbps_dis}     

    ```**"""
        rep2 = requests.post(dis_webhook, data={"content":end_att})     
        end_email()
    else: 
        if pk<maxmbps:
            print("NO attacks detected!")
   




