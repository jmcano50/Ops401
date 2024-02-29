#!/bin/python3

import requests

# ANSI escape codes for colors
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"

def check_xss_vulnerability(url):
    try:
        # Define payload for testing XSS
        payload = "<script>alert('XSS Vulnerability Detected!');</script>"
        
        # Send a GET request to the target URL with the payload
        response = requests.get(url)
        
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(COLOR_RED + "[+] XSS Vulnerability Detected in:" + url + COLOR_RESET)
        else:
            print(COLOR_GREEN + "[-] No XSS Vulnerability Detected in:" + url + COLOR_RESET)
    except requests.RequestException as e:
        print(COLOR_RED + "[ERROR] Error occurred while connecting to the URL: " + str(e) + COLOR_RESET)

if __name__ == "__main__":
    while True:
        # Ask the user to input the target URL
        target_url = input("Enter the target URL to check for XSS vulnerability: ")
        
        # Check for XSS vulnerability
        check_xss_vulnerability(target_url)
        
        # Ask the user if they want to perform another search
        another_search = input("Do you want to check another URL for XSS vulnerability? (y/n): ").lower()
        if another_search != 'y':
            break
