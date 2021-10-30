"""
The program, referring to the DATA SET (named baby_names)
that contain ALL of the NAMES that were MOST POPULAR in at least one year, from 1900 to 2012, 
determines and displays the BOY'S name and the GIRL'S name 
given to the MOST CHILDREN born during a specific time period entered by the user.
"""


# Acquisition and Control of the DATA entered by the USER
while True:
    print("Enter the time PERIOD (1900-2012) in which you want to analyze BIRTHS")
    year_start = input("STARTING year: ")
    year_stop = input("FINAL year: ")
    if year_start.isdigit() and year_stop.isdigit():
        year_start = int(year_start)
        year_stop = int(year_stop)
        if 1900 <= year_start <= 2012 and 1900 <= year_start <= 2012 and \
                year_start <= year_stop:
            break


# FILES TO OPEN both for the BOYS and for GIRLS
for gender in range(2):
    # BOYS
    if gender == 0:
        postfix = "_BoysNames.txt"
        # Dictionary that will contain the most popular names (with relative births)
        gender_dict = boys_names = {}
    # GIRLS (gender == 1)
    else:
        postfix = "_GirlsNames.txt"
        # Dictionary that will contain the most popular names (with relative births)
        gender_dict = girls_names = {}

    # FILES TO OPEN for each year (from starting_year to final_year entered by the user)
    for i in range(int(year_start), int(year_stop)+1):
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

        # For each line name and number of births is stored (or updated) in the dictionary
        for name_frequency in f_name_opened.readlines():
            name = name_frequency.split(" ")[0]
            births = int(name_frequency.split(" ")[1])
            # Updating the item
            if name in gender_dict:
                gender_dict[name] += births
            # Storing the item
            else:
                gender_dict[name] = births

        # Closing the previously opened file
        f_name_opened.close()


# Displaying the RESULTS
print("MOST POPULAR NAME for BOYS born between 01/01/{} and 31/12/{} -> ".format(year_start, year_stop), end="")
boys_most_births = max(boys_names.values())
for name in boys_names:
    if boys_names[name] == boys_most_births:
        print(name + " ({} births)".format(str(boys_names[name]), end="  "))
print("MOST POPULAR NAME for GIRLS born between 01/01/{} and 31/12/{} -> ".format(year_start, year_stop), end="")
girls_most_births = max(girls_names.values())
for name in girls_names:
    if girls_names[name] == girls_most_births:
        print(name + " ({} births)".format(str(girls_names[name]), end="  "))
