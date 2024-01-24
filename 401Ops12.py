#!/usr/bin/env python3
# Script Name:                  Ops 06: Network Security Tool with Scapy part 2 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/17/2024      
# Purpose:                      This Python script Encrypts a file or a message
# Resources:                    https://chat.openai.com/share/20ab9c80-7aef-40c5-ae7c-fefab534fd71

from scapy.all import sr1, ICMP, IP, TCP, send
import ipaddress
    
# TCP Port Range Scanner
def tcp_port_scan(host_ip, port_list):
    for port in port_list:
        packet = IP(dst=host_ip)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=2, verbose=True)
        if response is None:
            print(f"Port {port}is filtered (no response).")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                # Send RST packet to close the connection
                send(IP(dst=host_ip)/TCP(dport=port, flags='R'), timeout=1, verbose=False)
                print(f"Port {port} is open.")
            elif response.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed.")

# ICMP Ping Sweep Tool
def icmp_ping_sweep(network):
    online_hosts = 0
    network = ipaddress.ip_network(network, strict=False) # strict=False allows to ignore the host bits
    for ip in network.hosts ():
        resp = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=False)
        if resp is None:
            print(f"is down or unresponsive")
        elif (resp.haslayer(ICMP) and resp.getlayer(ICMP).type == 3 and resp.getlayer(ICMP).code in [1, 2, 3, 9, 10,13]):
            print(f"{ip} is actively blocking ICMP traffic.")
        else:
            print(f"{ip} is responding.")
            online_hosts += 1
    print(f"Total hosts online: {online_hosts}")

# Main function to handle user input and perform actions
def main():
    while True:
        print("\nselect a mode:")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        print("3. Exit")
        mode =input("Enter the mode (1/2/3): ")

        if mode == '1':
            host_ip = input("Enter the host IP to scan: ")
            ports = input("Enter the port range (e.g., 20-80) or specific ports seperated by commas: ")
            if '-' in ports:
                start_port, end_port = map(int, ports.split('-'))
                port_list = range(start_port, end_port + 1)
            else:
                port_list = [int(port.strip()) for port in ports.split(',')]
            tcp_port_scan(host_ip, port_list)
        elif mode == '2':
            network =input("Enter the network address with CIDR (e.g., 192.168.1.0/24): ")
            icmp_ping_sweep(network)
        elif mode == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid mode. Please choose a number between 1 and 3.")

if __name__ == "__main__":
    main()