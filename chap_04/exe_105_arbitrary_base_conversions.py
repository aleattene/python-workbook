"""
Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and the result number.
If the user chooses a base outside of this range then
an appropriate error message should be displayed and the program should exit.
Divide your program into several functions, including:
- a function that converts from an arbitrary base to base 10,
- a function that converts from base 10 to an arbitrary base, and
- a main program that reads the bases and input number from the user.
"""


# START Definition of the FUNCTIONS


def checkBase(base):                # Check BASES entered
    if base.isdigit():
        if 2 <= int(base) <= 16:
            return True
    return False


def checkNumber(number, base):      # Check NUMBER entered
    base = int(base)
    if 2 <= base <= 10:
        for i in number:
            if ord(i) < 48 or ord(i) > 57:
                return False
    elif 11 <= base <= 16:
        for i in number:
            if ord(i.upper()) < 48 or 58 <= ord(i.upper()) <= 64 or ord(i.upper()) >= (55 + base):
                return False
    return True


def baseToDecimal(number, base_number):     # CONVERSION BASE 2 -> BASE 10
    base_number = int(base_number)
    number_converted = 0
    position = 0
    for i in reversed(number):
        if 48 <= ord(i) <= 57:
            number_converted += int(i) * (base_number ** position)
            position += 1
        else:   # 65 <= ord(i) <= 70:
            number_converted += (ord(i.upper())-55) * (base_number ** position)
            position += 1
    return number_converted


def decimalToBase(number, base_conversion):     # CONVERSION BASE 2 -> BASE 10
    number = int(number)
    base_conversion = int(base_conversion)
    if number == 0:
        return "0"
    number_converted_tmp = []
    while number != 0:
        digit = number % base_conversion
        if 0 <= digit <= 9:
            number_converted_tmp.append(str(digit))
        else:        # 10 <= hex_digit <= 15:
            number_converted_tmp.append(chr(digit + 55))
        number = number // base_conversion
    number_converted = "".join(reversed(number_converted_tmp))
    return number_converted


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    number = input("Enter a NUMBER: ")
    base_number = input("Enter the BASE of the NUMBER just entered: ")
    base_conversion = input(
        "Enter the BASE where you want to CONVERT the number you just entered: ")
    base_number_checked = checkBase(base_number)
    base_conversion_checked = checkBase(base_conversion)
    number_checked = checkNumber(number, base_number)

    while not(base_number_checked and base_conversion_checked and number_checked):
        print("Incorrect entry. Try again.")
        number = input("Enter a NUMBER: ")
        base_number = input("Enter the BASE of the NUMBER just entered: ")
        base_conversion = input(
            "Enter the BASE where you want to CONVERT the number you just entered: ")
        base_number_checked = checkBase(base_number)
        base_conversion_checked = checkBase(base_conversion)
        number_checked = checkNumber(number, base_number)

    # NUMBER CONVERSION
    if base_number == "10":
        number_converted = decimalToBase(number, base_conversion)
    elif base_conversion == "10":
        number_converted = baseToDecimal(number, base_number)
    else:
        number_converted = baseToDecimal(number, base_number)
        number_converted = decimalToBase(number_converted, base_conversion)

    # Displaying the CONVERSION RESULT
    print("The NUMBER {} (base {}) is equal to {} (base {}).".format(
        number, base_number, number_converted, base_conversion))


if __name__ == "__main__":
    main()
