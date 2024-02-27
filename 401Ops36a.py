import subprocess

# Colors for better readability
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def netcat_banner_grabbing(target, port):
    try:
        output = subprocess.check_output(['nc', '-v', '-z', '-w', '5', target, str(port)])
        print("{}[*] Banner Grabbing using Netcat:{}".format(bcolors.OKGREEN, bcolors.ENDC))
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("{}[!] Error occurred during Netcat banner grabbing: {}{}".format(bcolors.FAIL, e, bcolors.ENDC))

def telnet_banner_grabbing(target, port):
    try:
        output = subprocess.check_output(['timeout', '10', 'telnet', target, str(port)], stderr=subprocess.STDOUT)
        success_message = "Connected to {}".format(target)
        if success_message in output.decode():
            print("{}[*] Banner Grabbing using Telnet: Connection Successful{}".format(bcolors.OKGREEN, bcolors.ENDC))
        else:
            print("{}[*] Banner Grabbing using Telnet:{}".format(bcolors.OKGREEN, bcolors.ENDC))
        print(output.decode())
    except subprocess.CalledProcessError as e:
        if e.returncode == 124:  # Timeout command exit code for a timeout
            print("{}[*] Banner Grabbing using Telnet: Connection Timed Out (Potentially Successful){}".format(bcolors.WARNING, bcolors.ENDC))
            print(e.output.decode())
        else:
            print("{}[!] Error occurred during Telnet banner grabbing: {}{}".format(bcolors.FAIL, e.output.decode(), bcolors.ENDC))

def nmap_banner_grabbing(target):
    try:
        output = subprocess.check_output(['nmap', '-sV', target])
        print("{}[*] Banner Grabbing using Nmap:{}".format(bcolors.OKGREEN, bcolors.ENDC))
        print(output.decode())
    except subprocess.CalledProcessError as e:
        print("{}[!] Error occurred during Nmap banner grabbing: {}{}".format(bcolors.FAIL, e.output.decode(), bcolors.ENDC))

def main():
    target = input("{}Enter the URL or IP address (e.g., scanme.nmap.org): {}".format(bcolors.HEADER, bcolors.ENDC))
    port = input("{}Enter the port number (e.g., 80): {}".format(bcolors.HEADER, bcolors.ENDC))

    netcat_banner_grabbing(target, port)
    telnet_banner_grabbing(target, port)
    nmap_banner_grabbing(target)

if __name__ == "__main__":
    main()
