# 
This template is useful for monitoring input traffic to the server by reading server logs. </br>
- It reads the log file. For Simplicity I have pasted contents from a logfile into access_log.
- Count number of requests to the server from each traffic IP.
- Store the output into a csv file as a report.

# How to use
` python3 log_parser.py --logfile <path_to_logfile> `
for ease, </br>
Run ` python3 log_parser.py --logfile access_log `

Alternatively access your logfiles, </br>
- /var/log/nginx
- var/log/apache2/
etc.

# Output
A new file named * Traffic_IP.csv * with contents </br>
```
IP_Address |,| Occurrence
107.0.0.0,5
127.0.0.1,2
127.0.0.0,1
```
