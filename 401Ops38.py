#!/usr/bin/env python3
# Author: Your Name
# Date: 2024-02-28
# Ops Challenge: XSS Vulnerability Detection with Python

"""This script attempts to detect XSS vulnerabilities in a given URL by injecting a simple XSS payload into form fields and checking if the payload is reflected in the response.
If the payload is reflected, it indicates a potential XSS vulnerability.
It uses colored output in the terminal to highlight the results."""

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

