#!/usr/bin/env python3
# Script Name:                  Ops Challenge: XSS Vulnerability Detection with Python
# Author:                       Juan Miguel Cano 
# Date of latest revision:      02/28/2024
# Resource:                     https://chat.openai.com/share/0ab8a8fd-8897-4c27-b246-f37adf0412fc
# Purpose:                      
"""The purpose of this script is to check a given URL for XSS (Cross-Site Scripting) vulnerabilities 
by sending a payload and analyzing the response for potential script injection."""


import requests
import re

# ANSI escape codes for colors
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_RESET = "\033[0m"

def check_xss_vulnerability(url):
    try:
        # Add schema if not provided in the URL
        if not re.match(r'^https?://', url):
            url = 'http://' + url

        # Define payload for testing XSS
        payload = "<script>alert('XSS Vulnerability Detected!');</script>"
        
        # Send a GET request to the target URL
        response = requests.get(url)
        
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(COLOR_RED + "[XSS Detected] Potential XSS vulnerability found in:" + COLOR_RESET, url)
        else:
            print(COLOR_GREEN + "[No XSS] No XSS vulnerability detected in:" + COLOR_RESET, url)
    except requests.RequestException as e:
        print(COLOR_YELLOW + "[Error] Error occurred while connecting to the URL:" + COLOR_RESET, str(e))

if __name__ == "__main__":
    while True:
        # Ask the user to input the target URL
        target_url = input(COLOR_YELLOW + "Enter the target URL to check for XSS vulnerability: " + COLOR_RESET)
        
        check_xss_vulnerability(target_url)
        
        # Ask the user if they want to perform another search
        another_search = input(COLOR_YELLOW + "Do you want to check another URL for XSS vulnerability? (y/n): " + COLOR_RESET).lower()
        if another_search != 'y':
            break

