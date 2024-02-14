#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Ops Challenge: Event Logging Tool Part 3 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      02/13/2024
# Purpose:                      StreamHandler and FileHandler 
# Purpose:                      Incorporating logging capabilities using handlers for both timed rotating file logs and regular file logs, alon with logging to the terminal.
# Purpose 2:                    Demonstrate the manipulation of lists and the use of various list methods, including basic operations and involving tuples, sets, and dictionaries.                    
# Execution:                    301Ops8.py
# Resource:                     https://chat.openai.com/share/35f7747d-4bc3-4c85-9845-612d7913c439
# Team member:                  Rodolfo Gonzalez

import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir"
    logmsg += str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Step 1: Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logging.info('Printed the fourth element of the list')

# Rest of the script remains the same



