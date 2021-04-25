"""
The program READS a FILE containing information about CHEMICAL ELEMENTS
and stores it in one appropriate data structure.
After that reads and process INPUT from the USER:
- if the user enters an INTEGER, it displays the SYMBOL and the NAME 
    of the element with that number of protons
- if the user enters a NON-INTEGER value, it displays the NUMBER of PROTONS
    for the element with that name or symbol
- if NO ELEMENT exists for the name, symbol or protons entered, 
    it displays an appropriate ERROR MESSAGE
The inserting continues until a blank line is entered by the user.
"""

# FILE TO OPEN
FILE_TO_OPEN = "elements.txt"

# Opening the file
open_file = True
while open_file:
    try:
        f_name_opened = open(FILE_TO_OPEN, "r")
        open_file = False
    # Exception -> file not found
    except FileNotFoundError:
        print("Warning, the file \"{}\" wasn't found.".format(FILE_TO_OPEN))
        quit()


# LIST which will contain the CHEMICAL ELEMENTS
chemical_elements = []

# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Adding the line (list) to the list that contain the CHEMICAL ELEMENTS
    chemical_elements.append(line.strip().split(","))


# Closing the previously opened file
f_name_opened.close()


while True:
    # Acquisition of the file name by the user
    value = input("Enter a VALUE: ")
    # Blank line
    if value == "":
        break
    # Checking the presence of the value entered by the user in the list (CHEMICAL ELEMENTS)
    for i in range(len(chemical_elements)):
        if value in chemical_elements[i]:
            # Element present in the list
            element = chemical_elements[i]
            break
    # Element not present in the list
    else:
        element = ""

    # Displaying the RESULTS
    if element == "":
        print("WARNING, NO ELEMENT exists for the name, symbol or protons entered.")
    elif value.isdigit():
        print("Chemical element -> {} - {}".format(
            element[1], element[2]))
    else:
        print("Chemical element -> ({}) protons".format(
            element[0]))
