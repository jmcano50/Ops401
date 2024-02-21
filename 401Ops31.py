#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Singnature-based malware Detection Part 1 of 3
# Author:                       Juan Miguel Cano & Rodolfo Gonzalez
# Date of latest revision:      02/19/2024
# Team member:                  Rodolfo Gonzalez
# Purpose: 

"""This code serves as a utility for searching specific files within a given directory and its subdirectories, 
allowing the user to list all available directories"""

import os

def search_file(file_name, directory):
    hits = 0
    files_searched = 0

    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return 0, 0

    print(f"Searching for '{file_name}' in '{directory}'...")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits += 1
                file_path = os.path.join(root, file)
                print("Found:", file_path)
            files_searched += 1
            print_progress(files_searched)

    return hits, files_searched

def print_progress(files_searched):
    print(f"Files searched: {files_searched}", end='\r')

def list_directories():
    current_directory = os.getcwd()
    print("Available directories:")
    for item in os.listdir("/"):
        item_path = os.path.join("/", item)
        if os.path.isdir(item_path):
            if item_path == current_directory:
                print("- ", item_path, "(Current Directory)")
            else:
                print("- ", item_path)
    print()

def search_files():
    file_name = input("Enter the file name to search for: ").strip()
    directory = input("Enter the directory to search in or type 'list' to see available directories: ").strip()

    if directory.lower() == "list":
        list_directories()
        return

    if not file_name:
        print("Error: Please provide a file name.")
        return

    if not directory:
        print("Error: Please provide a directory.")
        return

    if not os.path.exists(directory):
        print("Error: Directory does not exist.")
        return

    hits, files_searched = search_file(file_name, directory)

    if hits == 0 and files_searched == 0:
        print("\nNo files searched due to directory error.")
    else:
        print("\nTotal files searched:", files_searched)
        print("Total hits found:", hits)

def main():
    while True:
        print("\nMenu:")
        print("1. Search for files")
        print("2. List available directories")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            search_files()
        elif choice == "2":
            list_directories()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
