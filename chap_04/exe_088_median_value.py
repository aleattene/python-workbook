"""
The program receives THREE VALUES from the USER
and returns (displaying it) their MEDIAN.
"""


# START Definition of FUNCTIONS


def valutaEntry(number):
    # Check Entry -> INT or FLOAT
    return True


def medianThreeValues(num_1, num_2, num_3):
    min_value = min(num_1, num_2, num_3)
    max_value = max(num_1, num_2, num_3)
    if num_1 != min_value and num_1 != max_value:
        median = num_1
    elif num_2 != min_value and num_2 != max_value:
        median = num_2
    else:
        median = num_3
    return median


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
number_1 = input("Enter the FIRST NUMBER: ")
number_2 = input("Enter the SECOND NUMBER: ")
number_3 = input("Enter the THIRD NUMBER: ")
number_1_validated = valutaEntry(number_1)
number_2_validated = valutaEntry(number_2)
number_3_validated = valutaEntry(number_3)

while not(number_1_validated and number_2_validated and number_3_validated):
    print("Incorrect entry. Try again.")
    number_1 = input("Enter the FIRST NUMBER: ")
    number_2 = input("Enter the SECOND NUMBER: ")
    number_3 = input("Enter the THIRD NUMBER: ")
    number_1_validated = valutaEntry(number_1)
    number_2_validated = valutaEntry(number_2)
    number_3_validated = valutaEntry(number_3)


# NUMBERS conversion : STR -> FLOAT
number_1 = float(number_1)
number_2 = float(number_2)
number_3 = float(number_3)


# MEDIAN computing
median = medianThreeValues(number_1, number_2, number_3)


# Displaying the RESULT
print("The MEDIAN of the VALUES {0:.2f}, {1:.2f} and {2:.2f} is {3:.2f}".format(
    number_1, number_2, number_3, median))
