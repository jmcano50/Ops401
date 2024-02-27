import re

def search_cve_in_text(text):
    # This pattern will match strings like CVE-1999-0067 or CVE-2021-34527
    cve_pattern = r'CVE-\d{4}-\d{4,7}'
    return re.findall(cve_pattern, text)

# Replace 'path_to_log_file.txt' with the actual path to your log file
log_file_path = 'path_to_log_file.txt'

try:
    with open(log_file_path, 'r') as file:
        log_text = file.read()
    
    # Search for CVEs in the log text
    cve_matches = search_cve_in_text(log_text)
    
    if cve_matches:
        print("Found CVEs:", cve_matches)
    else:
        print("No CVEs found in the log text.")

except FileNotFoundError:
    print(f"The file {log_file_path} does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
