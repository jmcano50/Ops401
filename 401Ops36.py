import subprocess

# Colors for better readability
class bcolors:
    HEADER = '\033[96m'  # Cyan
    OKBLUE = '\033[94m'  # Blue
    OKGREEN = '\033[92m'  # Green
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'  # Red
    ENDC = '\033[0m'  # Reset to default color
    BOLD = '\033[1m'  # Bold
    UNDERLINE = '\033[4m'  # Underline

# Function to perform banner grabbing
def banner_grabbing(target, port):
    try:
        # Running nmap command with subprocess.run
        nmap_command = ['nmap', '-sV', '-p', str(port), '-Pn', target]
        result = subprocess.run(nmap_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

        # Output the result with colors
        print(f"{bcolors.OKGREEN}Banner Grabbing Output:{bcolors.ENDC}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{bcolors.FAIL}An error occurred while trying to run nmap:{bcolors.ENDC}")
        print(e.stderr)

# Main function to get user input and call the banner grabbing function
def main():
    # Getting user input
    target = input(f"{bcolors.HEADER}Enter the URL or IP address (e.g., scanme.nmap.org): {bcolors.ENDC}")
    port = input(f"{bcolors.OKBLUE}Enter the port number (e.g., 80): {bcolors.ENDC}")

    # Perform banner grabbing
    banner_grabbing(target, port)

# Entry point of the script
if __name__ == "__main__":
    main()
