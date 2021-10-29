"""
The program READS a FILE 
and displays it so that each line is as full as possible in a terminal window 
(for example having the width of 50 characters).
"""


open_file = True
while open_file:
    # FILE TO OPEN
    file_to_open = "alice_adventures_wonderland.txt"

    try:
        # Opening the file in reading mode
        f_name_opened = open(file_to_open, "r")
        open_file = False

    # Exception -> file not found
    except FileNotFoundError:
        print("Warning, the file \"{}\" wasn't found.".format(file_to_open))
        quit()


# List that will contain the words presents in the file (including the lines empty)
all_text = []


# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Selection of every word in every line
    for word in line.split(" "):
        all_text.append(word)


# Closing the previously opened file
f_name_opened.close()


# Width of the terminal window
MAXIMUM_LENGHT = 50


# Displayng the RESULTS
line = ""
for word in all_text:
    # The word is a new paragraph
    if word.strip() == "":
        print(line)
        print(word.strip())
        line = ""
        continue
    # The word goes to compose the line
    line_tmp = line
    line_tmp += word.strip() + " "
    # (until the line width do not exceed the width of the terminal window)
    if len(line_tmp) > MAXIMUM_LENGHT:
        # width exceeded -> line is printed without the new word
        print(line)
        # The word goes to compose the new line
        line_tmp = line
        line = word.strip() + " "
        continue
    # width not exceeded -> The word continues to compose the line
    else:
        line = line_tmp
