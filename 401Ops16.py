#!/usr/bin/env python3
# Script Name:                  Ops 16: Automated Brute Force Wordlist Attack Tool Part 1 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      01/29/2024      
# Purpose:                      Provides two modes for interacting with a word list file, 
# Purpose cont:                 allowing users to either iterate through the list with delays (simulating a dictionary attack) 
# Purpose cont:                 or search for specific words with in the list
# Resources:                    https://chat.openai.com/share/6fa45c27-3231-47cf-a6fa-3d855cf80f79                    

import time

#Function to perfor Mode 1: Offensive; Dictionary Iterator
def offensive_mode(file_path):
   delay = float(input("Enter the delay between words (in seconds): "))
   try:
        with open(file_path, 'rb') as file: # Open in binary mode
           while True:
                word = file.readline().decode('utf-8', errors='ignore').strip()
                if not word:
                    break
                print(word)
                time.sleep(delay)
   except FileNotFoundError:
        print("File not found.")

# Function to perform Mode 2: Defensive; Password Recognized
def defensive_mode(file_path):
    user_input = input("Enter a word to search: ")
    try:
        with open(file_path, 'rb') as file: # Open in binary mode
            while True:
                line = file.readline()
                if not line:
                    break
                word = line.decode('utf-8', errors='ignore').strip()
                if user_input == word:
                    print("The word is in the word list.")
                    return
            print("The word is not in the word list.")
    except FileNotFoundError:
        print("File not found.")
                                                              
if __name__ == "__main__":
   mode = input("Select a mode (1 for Offensive, 2 for Defensive): ")
   file_path = "rockyou.txt" # The word file is in this directory

   if mode == '1':
        offensive_mode(file_path)
   elif mode == '2':
        defensive_mode(file_path)
   else:
        print("Invalid mode selection. Please choose 1 or 2.")