# packet-detection
This program written in Python detects incoming Denial of Service Attack (DoS) / Distributed Denial of Service Attack (DDoS), By monitoring the incoming Traffic / Packets into your server and if the packet rate spikes and there is a attack, it Emails the users or sends a message in your Discord server using the Webhook.

Setup- 

1) apt update && apt upgrade

2) apt install iptables

3) iptables -A FORWARD -i tun0 -o eth0 -j ACCEPT          #only forward the interface if you have a VPN server

4) apt install screen 

5) screen python3 detection.py

6) To setup email - https://www.youtube.com/watch?v=g_j6ILT-X0k
