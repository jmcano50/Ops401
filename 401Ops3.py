# Script Name:                  Ops 02: Uptime Sensor Tool Part 2 of 2
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/10/2024      
# Purpose:                      This Python script is to monitor the availability of a specified IP address by sending periodic ICMP(ping) packets and recording the status in a log file, providing a simple way to check if a hos is up or down on a LAN.
# Resources:                    https://chat.openai.com/share/bf3f7e53-d92c-45a7-b021-425669de004c

import os
import time
import smtplib
import getpass
from email.mime.text import MIMEText

def ping_host(target_ip):
    return os.system(f"ping -c 1 {target_ip} > /dev/null 2>&1")

def send_email(sender_email, password, recipient_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

if __name__ == "__main__":
    target_ip = input("Enter the target IP address to monitor: ")
    log_filename = "uptime_log.txt"
    sender_email = input("Enter the sender email address to monitor: ")
    password = getpass.getpass("Enter your email App password: ")
    recipient_email = sender_email # Assuming the sender is also the recipient

    previous_status = None

    try:
        with open(log_filename, "a") as log_file:
            while True:
                exit_code = ping_host(target_ip)
                current_status = "Active" if exit_code == 0 else "Inactive"
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                if current_status != previous_status and previous_status is not None:
                    subject = f"Status Change Detected for {target_ip}"
                    body =f"{timestamp}: Host {target_ip} changed status from  {previous_status} to {current_status}"
                    send_email(sender_email, password, recipient_email, subject, body)

                print(f"{timestamp} Network {current_status} to {target_ip}")
                log_file.write(f"{timestamp} Network {current_status} to {target_ip}\n")
                log_file.flush()

                previous_status = current_status
                time.sleep(10) # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("Monitoring stopped.")            
                