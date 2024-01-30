# Open the original "rockyou.txt" file for reading
with open('rockyou.txt', 'r') as original_file:
    # Specify the number of lines you want to extract
    num_lines_to_extract = 1000  # Adjust this number as needed

    # Read the specified number of lines from the original file
    lines_to_extract = [next(original_file) for _ in range(num_lines_to_extract)]

# Open a new file for writing the extracted lines
with open('smaller_rockyou.txt', 'w') as new_file:
    # Write the extracted lines to the new file
    new_file.writelines(lines_to_extract)

