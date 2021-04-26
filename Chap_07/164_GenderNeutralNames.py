"""
The program, referring to the DATA SET (named BabyNames) that contain ALL of the NAMES 
that were MOST POPULAR in at least one year, from 1900 to 2012, 
determines and displays all of the NAMES that were USED for both BOYS and GIRLS
in a specific YEAR entered by the USER.
"""


while True:
    # Acquisition and Control of the DATA entered by the USER
    year = input("Enter a YEAR from 1900 to 2012 (blank line to quit): ")
    if year == "":  # Empty line
        break
    # FILES TO OPEN both for the BOYS and for GIRLS
    FILE_TO_OPEN_BOYS = ".\BabyNames\\" + str(year) + "_BoysNames.txt"
    FILE_TO_OPEN_GIRLS = ".\BabyNames\\" + str(year) + "_GirlsNames.txt"

    # Opening the files in reading mode
    open_file = True
    while open_file:
        try:
            f_name_boys_opened = open(FILE_TO_OPEN_BOYS, "r")
            f_name_girls_opened = open(FILE_TO_OPEN_GIRLS, "r")
            open_file = False
        # Exception -> file not found
        except FileNotFoundError:
            print("I'm sorry, there is no information for the year entered.")
            quit()
            # Possible evolution -> handle exception in a manner more specific

    # Population of the list with the names of the boys
    boys_names = []
    for line_boys in f_name_boys_opened.readlines():
        if line_boys.split(" ")[0] not in boys_names:
            boys_names.append(line_boys.split(" ")[0])
    # Population of the list with the gender neutral names
    neutral_gender_names = []
    for line_girls in f_name_girls_opened.readlines():
        if line_girls.split(" ")[0] in boys_names and \
                line_girls.split(" ")[0] not in neutral_gender_names:
            neutral_gender_names.append(line_girls.split(" ")[0])

    # Closing the previously opened files
    f_name_boys_opened.close()
    f_name_girls_opened.close()

    # Displaying the RESULTS
    if len(neutral_gender_names) == 0:
        print(
            "There aren't ANY GENDER neutral NAMES for the entered YEAR ({}).".format(year))
    elif len(neutral_gender_names) == 1:
        print("For the year {}, the ONLY gender-neutral NAME is {}.".format(
            year, neutral_gender_names[0]))
    else:
        print("For the year {}, the gender-neutral NAMES are: ".format(year), end="")
        for name in neutral_gender_names:
            print(name, end="  ")
        print()
