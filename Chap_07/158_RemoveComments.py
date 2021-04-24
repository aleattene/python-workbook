"""
The program removes all of the COMMENTS from a Python Source FILE
and save the modified code in a new Python FILE.
Both the names of the FILES are entered by the USER.
"""

# Acquisition and Control of the DATA entered by the USER
while True:
    try:
        # Python Source File name
        file_to_read = input("Enter the FILE name to be analyzed: ")
        # Opening the origin file in read mode
        f_name_read_opened = open(file_to_read, "r")
        # Python File name
        file_to_write = input("Enter the FILE name to WRITE: ")
        # Opening or Creating the destination file in write mode
        f_name_write_opened = open(file_to_write, "w")
        break
    # Exception Type -> File not found
    except FileNotFoundError:
        print("Warning, at least one file entered wasn't found.")
        # Possible evolution -> handle exception for each file inserted

# Each line in the source file, if it is not a comment, is stored in a new file
for line in f_name_read_opened.readlines():
    if len(line.strip()) > 0:
        if line.strip()[0] == "#":
            continue
    f_name_write_opened.write(line)

# Closing opened files
f_name_read_opened.close()
f_name_write_opened.close()

# Opening and reading of the previously written file
with open(file_to_write, "r") as file_written:
    print(file_written.read().encode("latin-1").decode("utf-8"))
