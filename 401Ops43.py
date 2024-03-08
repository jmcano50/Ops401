#!/usr/bin/env python3
# Script Name:                  Ops 42: Create a Port Scanner
# Author:                       Juan Miguel Cano
# Date of latest revision:      03/06/2024
# Attributions:                 Rodolfo Gonzalez
# Resources:                    https://chat.openai.com/share/ab539535-2caf-426e-90ca-85fc81e3a292
# Purpose:
'''The purpose of the script is to create a port scanner, allowing users to scan a range fo ports 
    on a specified host IP address to determine which ports are open or closed.'''

import socket
import concurrent.futures
import ipaddress

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def scan_port(hostip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockmod:
            sockmod.settimeout(1)  # Set a timeout value
            result = sockmod.connect_ex((hostip, port))
            if result == 0:
                print(f"Port {port} {GREEN}open{RESET}")
            elif result == 111:  # Connection refused
                print(f"Port {port} {RED}closed{RESET}")
            else:
                print(f"Port {port} status: {RED}{result}{RESET}")
    except socket.error as e:
        print(f"Error while scanning port {port}: {RED}{e}{RESET}")

def portScanner(hostip, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on host {hostip}...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda port: scan_port(hostip, port), range(start_port, end_port + 1))

if __name__ == "__main__":
    try:
        hostip = input("Enter the host IP: ")  # Collect host IP from the user
        ipaddress.ip_address(hostip)  # Validate the entered IP address
    except ValueError:
        print(f"{RED}Invalid IP address format.{RESET}")
        exit(1)

    try:
        port_range = input("Enter the port range (start-end): ")  # Collect port range from the user
        start_port, end_port = map(int, port_range.split('-'))
        if not (0 < start_port <= end_port <= 65535):
            raise ValueError("Invalid port range.")
    except (ValueError, IndexError):
        print(f"{RED}Invalid port range format.{RESET}")
        exit(1)

    portScanner(hostip, start_port, end_port)