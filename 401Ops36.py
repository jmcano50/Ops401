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

def banner_grabbing(command, target, port):
    try:
        # If port is an empty string, do not include it in the command
        cmd = command + [target] if port == '' else command + [target, str(port)]
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)
        print(f"{bcolors.OKGREEN}[*] Banner Grabbing: Connection Successful{bcolors.ENDC}")
        print(output.decode())
    except subprocess.TimeoutExpired:
        print(f"{bcolors.WARNING}[*] Banner Grabbing: Connection Timed Out (Potentially Successful){bcolors.ENDC}")
    except subprocess.CalledProcessError as e:
        print(f"{bcolors.FAIL}[!] Error occurred:{bcolors.ENDC}", e.output.decode())

def main():
    target = input(f"{bcolors.HEADER}Enter the URL or IP address (e.g., scanme.nmap.org): {bcolors.ENDC}")
    port = input(f"{bcolors.OKBLUE}Enter the port number (e.g., 80): {bcolors.ENDC}")

    banner_grabbing(['nc', '-v', '-z', '-w', '5'], target, port)
    banner_grabbing(['timeout', '10', 'telnet'], target, port)

    # Updated nmap command to include error handling flags and verbose
    banner_grabbing(['nmap', '-sV', '-Pn', '--unprivileged', '-vv'], target, port)

if __name__ == "__main__":
    main()
