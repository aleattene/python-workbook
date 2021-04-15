"""
The program receives a CANADIAN POSTAL CODE from the USER
and returns (displaying it) the PROVINCE or TERRITORY ASSOCIATED with it,
along with WHETHER the ADDRESS is URBAN or RURAL.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):
    # Possible evolution -> CHECK ENTRY -> valid characters
    pass


def checkPostalCode(text_message):
    # DICTIONARY - FIRST CHARACTER of CANADIAN POSTAL CODE
    canadians_provinces = {
        "A": "Newfoundland",
        "B": "Nova Scotia",
        "C": "Prince Edward Island",
        "E": "New Brunswick",
        "G": "Quebec",
        "H": "Quebec",
        "J": "Quebec",
        "K": "Ontario",
        "L": "Ontario",
        "M": "Ontario",
        "N": "Ontario",
        "P": "Ontario",
        "R": "Manitoba",
        "S": "Saskatchewan",
        "T": "Alberta",
        "V": "British Columbia",
        "X": "Nunavut",
        "X": "Northwest Territories",
        "Y": "Yukon"
    }
    # LIST ["canadian province","type_territory" ]
    province_territory = []
    # Evaluation of the first character of the Canadian Postal Code
    if text_message[0].upper() in canadians_provinces:
        province_territory.append(canadians_provinces[text_message[0].upper()])
        # Evaluation of the second character of the Canadian Postal Code
        if text_message[1] == "0":
            province_territory.append("a rural")
        elif "1" <= text_message[1] <= "9":
            province_territory.append("an urban")
    return province_territory


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    text_message = input("Enter the TEXT MESSAGE: ")
    # STRING TESTING
    # text_message = "T2N 1N4"
    # text_message = "X0A 1B2"
    # STRING TESTING - INVALID POSTAL CODE
    # text_message = "D2N 1N4"
    # text_message = "TAN 1N4"

    # LIST ["canadian province","type_territory" ]
    address_postal_code = checkPostalCode(text_message)

    # Displaying the RESULT
    if len(address_postal_code) < 2:
        print("WARNING, you have entered an INVALID POSTAL CODE.")
    else:
        print("The POSTAL CODE {} is for {} address in {}.".format(
            text_message.upper(), address_postal_code[1], address_postal_code[0]))


if __name__ == "__main__":
    main()
