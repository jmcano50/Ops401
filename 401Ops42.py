#!/usr/bin/env python3
# Script Name:                  Ops 42: Attack Tools Part 2 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      03/05/2024
# Attributions:                 Rudolfo Gonzalez
# Resouces:                     https://chat.openai.com/share/a5d10412-571c-464f-a7cf-f3e258c5a21f
# Purpose:                      

'''The purpose of this script is to automate Nmap scanning operations for specified IP address
    and port ranges providing options for various scan types.'''

import os
import sys
import nmap
from colorama import init, Fore, Style
import subprocess

# Initialize colorama for colored output
init()

def elevate_privileges():
    """Elevate privileges to root using sudo."""
    script_path = os.path.abspath(sys.argv[0])
    subprocess.call(['sudo', sys.executable, script_path] + sys.argv[1:])
    sys.exit()

# Check if the script is running with root privileges
if os.geteuid() != 0:
    print(Fore.RED + "This script requires root privileges to perform certain scan types.")
    print("Attempting to elevate privileges..." + Style.RESET_ALL)
    elevate_privileges()

scanner = nmap.PortScanner()

print(Fore.MAGENTA + "Nmap Automation Tool" + Style.RESET_ALL)
print("--------------------")

ip_addr = input("Enter the IP address to scan: ")
print("The IP you entered is:", ip_addr)

print(Fore.MAGENTA + "\nSelect scan to execute:")
print("1) SYN ACK Scan")
print("2) UDP Scan")
print("3) TCP Connect Scan" + Style.RESET_ALL)

resp = input("You have selected option: ")

port_range = input("Enter port range (e.g., 1-100): ")

# Validate port range input
if not port_range.replace('-', '').isdigit():
    print(Fore.RED + "Invalid port range format. Please enter a valid range like '1-100'." + Style.RESET_ALL)
    sys.exit(1)

if resp in ['1', '2', '3']:
    scan_types = {'1': ('-v -sS', 'tcp'), '2': ('-v -sU', 'udp'), '3': ('-v -sT', 'tcp')}
    scan_args, protocol = scan_types[resp]

    print(Fore.GREEN + "Nmap Version:", '.'.join(map(str, scanner.nmap_version())) + Style.RESET_ALL)
    
    try:
        scanner.scan(ip_addr, port_range, scan_args)
        print(scanner.scaninfo())
        print(Fore.GREEN + "IP Status:", scanner[ip_addr].state() + Style.RESET_ALL)
        print(scanner[ip_addr].all_protocols())
        
        if protocol in scanner[ip_addr]:
            open_ports = list(scanner[ip_addr][protocol].keys())
            print(Fore.GREEN + "Open Ports:", ", ".join(map(str, open_ports)) + Style.RESET_ALL)
        else:
            print(Fore.RED + f"No open {protocol.upper()} ports found." + Style.RESET_ALL)
    except nmap.nmap.PortScannerError as e:
        print(Fore.RED + "An error occurred during scanning:", e + Style.RESET_ALL)
else:
    print(Fore.RED + "Please enter a valid option" + Style.RESET_ALL)
