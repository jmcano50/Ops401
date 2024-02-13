#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Ops Challenge: Event Logging Tool Part 2 of 3
# Author:                       Juan Miguel Cano
# Date of latest revision:      02/13/2024
# Purpose:                      Incorporating logging capabilities into one of your existing Python tools.
# Purpose 2:                    Demonstrate the manipulation of lists and the use of various list methods, including basic operations and involving tuples, sets, and dictionaries.                    
# Execution:                    301Ops8.py
# Resource:                     https://chat.openai.com/share/b15c3ed2-a523-4434-ac9d-234befe35207
# Team member:                  Rodolfo Gonzalez
import logging
from logging.handlers import RotatingFileHandler
import os
import time

# Configure logging settings
logging.basicConfig(filename='collections_tool.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create and configure handler for rotating file logs
logger = logging.getLogger('myLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for rotating file logs
handler = RotatingFileHandler('collections_tool.log',maxBytes=5*1024*1024, backupCount=3)

for i in range(5): # Adjust range as needed
    logmsg = "Aye Aye Sir"
    logmsg +=str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)



# Step 1: Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logging.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logging.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logging.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logging.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logging.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logging.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logging.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logging.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logging.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logging.info('Removed an element at index 3 from the list')

# Use the remove() method to remove a specific element
try:
    original_list.remove("SSgt")
    print("List after removing 'SSgt':", original_list)
    logging.info('Removed "SSgt" from the list')
except ValueError:
    print("Cannot remove 'SSgt' from the list: 'SSgt' is not in the list")
    logging.warning("'SSgt' is not in the list")

# Use the reverse() method to reverse the order of elements in the list
original_list.reverse()
print("Reversed list:", original_list)
logging.info('Reversed the order of elements in the list')

# Use the sort() method to sort the elements in the list
original_list.sort()
print("Sorted list:", original_list)
logging.info('Sorted the list')

# Create a tuple
my_tuple = ("Pvt", "Pfc", "LCpl")

# Create a set
my_set = {"Pvt", "Pfc", "LCpl"}

# Create a dictionary
my_dict = {"Marines1": "Pvt", "Marines2": "Pfc", "Marines3": "LCpl"}

# Print the created tuple, set, and dictionary
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)