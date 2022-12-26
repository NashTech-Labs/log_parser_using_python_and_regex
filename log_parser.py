import re
from collections import Counter
import argparse
import csv

# log file input
input_log_file = argparse.ArgumentParser(description='Read logfile')
input_log_file.add_argument("--l","--logfile",
                       help='Enter the logfile to parse',dest="logfile",type=argparse.FileType('r'), required=True)
args = input_log_file.parse_args()

# regex to match IP address
log_regex="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
with args.logfile as input:
    fread = input.read()
    ip_list = re.findall(log_regex, fread)
# Store traffic IP in a csv file
    with open("Traffic_IP.csv", "w") as input:
        fwritercsv = csv.writer(input)
        fwritercsv.writerow(["IP_Address", "Count"])
        for k, v in Counter(ip_list).items():
            fwritercsv.writerow([k, v])