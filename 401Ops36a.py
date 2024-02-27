import subprocess

# Function to perform banner grabbing
def banner_grabbing(target, port):
    try:
        # Running nmap command with subprocess.run
        nmap_command = ['nmap', '-sV', '-p', str(port), '-Pn', target]
        result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # Output the result
        print("Banner Grabbing Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to run nmap:")
        print(e.stderr)

# Main function to get user input and call the banner grabbing function
def main():
    # Getting user input
    target = input("Enter the URL or IP address (e.g., scanme.nmap.org): ")
    port = input("Enter the port number (e.g., 80): ")

    # Perform banner grabbing
    banner_grabbing(target, port)

# Entry point of the script
if __name__ == "__main__":
    main()