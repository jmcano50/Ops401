#!/usr/bin/env python3
# Script Name:                  Ops 16: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/29/2024      
# Purpose:                      Provides two modes for interacting with a word list file, 
# Purpose cont:                 allowing users to either iterate through the list with delays (simulating a dictionary attack) 
# Purpose cont:                 or search for specific words within the list
# Resources:                    https://chat.openai.com/share/6fa45c27-3231-47cf-a6fa-3d855cf80f79                    

import time

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
                                                              
if __name__ == "__main__":
   mode = input("Select a mode (1 for Offensive, 2 for Defensive): ")
   file_path = "smaller_rockyou.txt"  # Use the smaller wordlist file as the wordlist

   if mode == '1':
        offensive_mode(file_path)
   elif mode == '2':
        defensive_mode(file_path)
   else:
        print("Invalid mode selection. Please choose 1 or 2.")
