"""
The program READS LINES from a FILE (whose name is entered by the USER),
adds line numbers to them 
and STORES the NUMBERED LINES into a NEW FILE 
(whose name is also entered by the USER).
"""

# Acquisition and Control of the DATA entered by the USER
while True:
    # File name to READ
    file_to_read = input("Enter the FILE name to READ: ")
    # File name to WRITE
    file_to_write = input("Enter the FILE name to WRITE: ")
    if file_to_read != "" and file_to_write != "":
        break

try:
    # Opening the origin file in read mode
    f_name_read_opened = open(file_to_read, "r")
    # Opening or Creating the destination file in write mode
    f_name_write_opened = open(file_to_write, "w")

    # Each line present in the origin file is stored in a new file
    i = 1
    for line in f_name_read_opened.readlines():
        f_name_write_opened.write(str(i) + ": " + line)
        i += 1

    # Closing open files
    f_name_read_opened.close()
    f_name_write_opened.close()

    # Opening and reading of the previously written file
    with open(file_to_write, "r") as file_written:
        print(file_written.read().encode("latin-1").decode("utf-8"))


# Exception Type -> File not found
except FileNotFoundError:
    print("Warning, the file entered wasn't found.")
    quit()
# Possible evolution -> handle exception for each file inserted
