# Script Name:                  Ops 02: Uptime Sensor Tool Part 1 of 2
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/09/2024      
# Purpose:                      This PowerShell script is to monitor the availability of a specified IP address by sending periodic ICMP(ping) packets and recording the status in a log file, providing a simple way to check if a hos is up or down on a LAN.
# Resources:                    https://chat.openai.com/share/be10bd55-5de3-4295-b0e7-ad45a62c94ee

import os
import time

def ping_host(target_ip):
    # Send a single ICMP (ping) packet and return the exit code
    return os.system(f"ping -c 1 {target_ip} > /dev/null 2>&1")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address to monitor: ")
    log_filename = "uptime_log.txt"

    try:
        with open(log_filename, "a") as log_file:
            while True:
                exit_code = ping_host(target_ip)

                # Determine status based on the exit code
                status = "Active" if exit_code == 0 else "Inactive"

                # Get the current timestamp with millisecond precision
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                # Print the status along with the timestamp and destination IP
                print(f"{timestamp} Network {status} to {target_ip}")

                # Save the output to the log file
                log_file.write(f"{timestamp} Network {status} to {target_ip}\n")
                log_file.flush()

                time.sleep(2)

    except KeyboardInterrupt:
            print("Monitoring stopped.")


# - [401Ops2a Screenshot](Photo_Screenshots/401Ops2a.png)
# - [401Ops2b Screenshot](Photo_Screenshots/401Ops2b.png)