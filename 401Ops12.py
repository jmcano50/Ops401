#!/usr/bin/env python3
# Script Name:                  Ops 06: Encryption file or message part 3 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/17/2024      
# Purpose:                      This Python script Encrypts a file or a message
# Resources:                    https://chat.openai.com/share/8d91c6a6-0cc4-4646-bc55-0e1efff0a96f




import os
import ctypes
from cryptography.fernet import Fernet, InvalidToken
from scapy.all import sr1, ICMP, IP, TCP, sr
import ipaddress
import subprocess

# Check if tkinter is available
try:
    import tkinter as tk
    from tkinter import messagebox
    tkinter_available = True
except ModuleNotFoundError:
    print("tkinter module not found. Ransomware simulation feature will be disabled.")
    
# Function to generate and save a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the existing encryption key
def load_key():
    return open("encryption_key.key", "rb").read()

# Function to encrypt a file using the provided key
def encrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = fernet.encrypt(file.read())
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file using the provided key
def decrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        decrypted_data = fernet.decrypt(file.read())
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt a string
def encrypt_string(text, key):
    return Fernet(key).encrypt(text.encode()).decode()

# Function to decrypt a string with error handling
def decrypt_string(text, key):
    try:
        return Fernet(key).decrypt(text.encode()).decode()
    except InvalidToken:
        return "Decryption failed: Invalid token. Check if the message is correct and the correct key is used."

# Function to change the desktop wallpaper
def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

# Function to create a popup window with a ransomware message (Windows only)
def show_ransomware_popup(message):
    if tkinter_available:
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Ransomware Alert", message)
        root.destroy()
    else:
        print("Ransomware message: ", message)

# Function to simulate a ransomware attack (Windows only)
def ransomware_simulation():
    wallpaper_image_path = "path_to_ransomware_wallpaper.jpg"
    ransomware_message = "Your files have been encrypted! To decrypt them, send 1 Bitcoin to..."
    change_wallpaper(wallpaper_image_path)
    show_ransomware_popup(ransomware_message)

# TCP Port Range Scanner
def tcp_port_scan(host_ip, port_list):
    for port in port_list:
        packet = IP(dst=host_ip)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=1, verbose=False)
    if response is None:
        print(f"Port {port}is filtered (no response).")
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12:
            # Send RST packet to close the connection
            send(IP(dst=host_ip)/TCP(dport=port, flags='R'), timeout=1, verbose=False)
            print(f"Port {port} is open.")
        elif response.getlayer(TCP).flags == 0x14:
            print(f"Port {port} is closed.")

# Function to perform ICMP Ping Sweep
def icmp_ping_sweep(network):
    online_hosts = 0
    network = ipaddress.ip_network(network, strict=False) # strict=False allows to ignore the host bits
    print(f"Scanning the network: {network}")
    for ip in network.hosts ():
        resp = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=False)
        if resp is None:
            print(f"Scanning the network: {network}")
        elif (int(resp.getlayer(ICMP).type) == 3 and
              int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
            print(f"{ip} is actively blocking ICMP traffic.")
        else:
            print(f"{ip} is responding.")
            online_hosts += 1
    print(f"Total hosts online: {online_hosts}")