"""
The program displays the NUMBER of ELEMENTS within a LIST (integers or floating-point numbers) 
that are GREATER than or equal to a MINIMUM VALUE and LESS than a MAXIMUM VALUE. 
"""


# START Definition of the FUNCTION


def countRange(original_values_list, min_value, max_value):
    list_numbers = original_values_list[:]  # copy list
    for i in range(len(list_numbers)):
        # Conversion [STR] -> [FLOAT]
        list_numbers[i] = float(list_numbers[i])
    # LIST SORTING
    list_numbers.sort()

    count = 0   # number of elements in RANGE (min_value -> max_value)
    for value in list_numbers:
        if min_value <= value < max_value:
            count += 1
        elif value >= max_value:
            break
    return count


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Declaratione of the VARIABLES / CONSTANTS
    MIN_VALUE = 3
    MAX_VALUE = 7

    # LIST of INTEGERS
    integers_list = ["1", "2", "3", "4", "0", "5", "7", "12", "8"]

    # LIST of FLOATING-POINT numbers
    floats_list = ["1.5", "2.4", "3.0", "0.5",
                   "0.9", "6.5", "7.0", "12.15", "8.9"]

    # possible evolution -> interaction with the user (input list_number, min_value and max_value)

    # Computing of the NUMBER of elements included between MIN_VALUE e MAX_VALUE
    range_integers = countRange(integers_list, MIN_VALUE, MAX_VALUE)
    range_float = countRange(floats_list, MIN_VALUE, MAX_VALUE)

    # Displaying the RESULTS
    print("NUMBER of INTEGERS having a VALUE " +
          "between {} and {} -> {}".format(MIN_VALUE, MAX_VALUE, range_integers))
    print("NUMBER of FLOATING-POINT numbers having a VALUE " +
          "between {} and {} -> {}".format(MIN_VALUE, MAX_VALUE, range_float))


if __name__ == "__main__":
    main()
