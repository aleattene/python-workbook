"""
The program receives from the USER a STRING
and returns (displaying it) whether or not it REPRESENTS an INTEGER
(ignoring any leading and trailing white spaces).
"""


# START Definition of the FUNCTIONS


def isInteger(numero):
    numero = numero.strip()     # removed leading and trailing white spaces
    if numero == "":
        return False
    elif len(numero) == 1 and numero.isdigit:
        return True
    elif len(numero) > 1:
        if numero.isdigit() or \
            (numero[0] == "-" and numero[1] != "0" and numero[1:].isdigit()) or \
                (numero[0] == "+" and numero[1] != "0" and numero[1:].isdigit()):
            return True


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # DATA acquisition (from USER)
    string = input("Enter the STRING (representing integer): ")

    # STRING evaluation (whether or not representing an INTEGER)
    string_integer = isInteger(string)

    # Displaying the RESULTS
    print("The STRING \"" + string.strip(), end="\"")
    if string_integer:
        print(" REPRESENTING the INTEGER {}.".format(int(string.strip())))
    else:
        print(" NOT REPRESENTING an INTEGER.")


if __name__ == "__main__":
    main()
