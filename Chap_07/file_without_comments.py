"""
The program READS LINES from a FILE (whose name is entered by the USER),
adds line numbers to them 
and STORES the NUMBERED LINES into a NEW FILE 
(whose name is also entered by the USER).
"""

while True:
    file_to_read = input("Enter the FILE name to READ: ")
    file_to_write = input("Enter the FILE name to WRITE: ")
    if file_to_read != "" and file_to_write != "":
        break

try:
    f_name_read_opened = open(file_to_read, "r")
    f_name_write_opened = open(file_to_write, "w")

    i = 1
    for line in f_name_read_opened.readlines():
        f_name_write_opened.write(str(i) + ": " + line)
        i += 1

    f_name_read_opened.close()
    f_name_write_opened.close()

    with open(file_to_write, "r") as file_written:
        print(file_written.read().encode("latin-1").decode("utf-8"))


except FileNotFoundError:
    print("Warning, the file entered wasn't found.")
    quit()
