"""
The program OPENS e READS every file present in the DATA SET (named baby_names)
that contains ALL of the NAMES that were MOST POPULAR in at least one year, from 1900 to 2012.
After that, it returns the MOST POPULAR NAMES both for the BOYS and for GIRLS.
"""


# FILES TO OPEN both for the BOYS and for GIRLS
for gender in range(2):
    # BOYS
    if gender == 0:
        postfix = "_BoysNames.txt"
        # List that will contain the most popular names
        gender_list = boys_names = []
    # GIRLS (gender == 1)
    else:
        postfix = "_GirlsNames.txt"
        # List that will contain the most popular names
        gender_list = girls_names = []

    # FILES TO OPEN for each year (from 1900 to 2012)
    for i in range(1900, 2013):
        FILE_TO_OPEN = ".\BabyNames\\" + str(i) + postfix

        # Opening the file in reading mode
        open_file = True
        while open_file:
            try:
                f_name_opened = open(FILE_TO_OPEN, "r")
                open_file = False
            # Exception -> file not found
            except FileNotFoundError:
                print("Warning, the file \"{}\" wasn't found.".format(FILE_TO_OPEN))
                quit()

        # Name selection from the first line (index zero of the list returned da readline/split methods)
        name = f_name_opened.readline().split(" ")[0]
        if name not in gender_list:
            # Name not present in the list
            gender_list.append(name)

        # Closing the previously opened file
        f_name_opened.close()


# Displaying the RESULTS
print("MOST POPULAR NAMES for BOYS -> ", end="")
for name in boys_names:
    print(name, end="  ")
print("\nMOST POPULAR NAMES for GIRLS -> ", end="")
for name in girls_names:
    print(name, end="  ")
