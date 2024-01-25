#!/usr/bin/env python3
# Script Name:                  Ops 13: Network Security Tool with Scapy part 3 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/24/2024      
# Purpose:                      Performs network scanning, including TCP port range scanning and ICMP ping sweeps, to ID open ports and active hosts on a network
# Resources:                    https://chat.openai.com/share/20ab9c80-7aef-40c5-ae7c-fefab534fd71

from scapy.all import sr1, ICMP, IP, TCP, send
import re

# Function to parse port range or list input
def parse_ports(port_input):
    if '-' in port_input:
        start_port, end_port = map(int, port_input.split('-'))
        return range(start_port, end_port +1)
    else:
        return [int(port.strip()) for port in port_input.split(',')]
    
# TCP Port Range Scanner
def tcp_port_scan(host_ip, port_list):
    for port in port_list:
        packet = IP(dst=host_ip)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=2, verbose=False) # Increased timeout for reliability
        if response is None:
            print(f"Port {port}is filtered (no response).")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                # Send RST packet to close the connection
                send(IP(dst=host_ip)/TCP(dport=port, flags='R'), verbose=False)
                print(f"Port {port} is open.")
            elif response.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed.")
        else:
            print(f"Port {port} is filtered and silently dropped.")

# ICMP Ping Function
def ping_host(host_ip):
    packet = IP(dst=host_ip)/ICMP()
    response = sr1(packet, timeout=1, verbose=False)
    if response:
        print(f"{host_ip} is up!")
        return True
    else:
        print(f"{host_ip} is down or not responding.")
        return False

# Main function to handle user input and perform actions
def main():
   host_ip = input("Enter the host IP to scan: ")
   if ping_host(host_ip):
       port_input = input("Enter the port range (e.g., 20-80) or specific ports seperated by commas: ")
       port_list = parse_ports(port_input)
       tcp_port_scan(host_ip, port_list)

if __name__ == "__main__":
    main()