# packet-detection
This program written in Python detects incoming Denial of Service Attack (DoS) / Distributed Denial of Service Attack (DDoS), By monitoring the incoming Traffic / Packets into your server and if the packet rate spikes and there is a attack, it Emails the users or sends a message in your Discord server using the Webhook.

Email Having trouble.

Setup- 

1) ``apt update && apt upgrade``

2) ``apt install iptables`` 

3) `` iptables -A FORWARD -i tun0 -o eth0 -j ACCEPT  ``        #only forward the interface if you have a VPN server

4) `` apt install screen ``

5) To setup email - https://youtu.be/90tn6zDfJCI

6) After you get your email and password put it in the program

7) You are all done now

8)`` screen python3 detection.py`` # now the program will run the the background
