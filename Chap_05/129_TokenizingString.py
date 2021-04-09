"""
The program converts a STRING entered by the USER
in a LIST of SUBSTRINGS (TOKENS), 
using the TOKENIZING process.
TOKENS are assumed to be identifiable as:
- mathematical operators -> + - * / ^
- parentheses -> ()
- integers
"""


# START Definition of the FUNCTIONS


def checkEntry(math_exp):      # possible evolution -> check entry
    pass


def tokenizingString(string):
    # LIST of the MATHEMATICAL OPERATORS
    tokens = ["+", "-", "*", "/", "^", "(", ")"]
    tokens_list = []
    i = 0
    while i < len(string):
        # Check MATHEMATICAL OPERATORS
        if string[i] in tokens and string[i] not in tokens_list:
            tokens_list.append(string[i])
        # Check INTEGERS
        elif string[i].isdigit():
            tmp = ""
            # LOOP for NUMBERS > 1 DIGITS
            while i < len(string):
                if string[i].isdigit():
                    tmp += string[i]
                    i += 1
                else:
                    i -= 1
                    break
            if tmp not in tokens_list:
                tokens_list.append(tmp)
        i += 1
    return tokens_list      # RETURN LIST of TOKENS


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    math_exp = input("Enter the MATHEMATICAL EXPRESSION: ")
    # STRING TESTING
    # math_exp = "1*(2 + (6 * (3-1)) / 844 + (74 ^ 3)) / 121-10+10"

    # Generation of the TOKENS LIST
    tokens_list = tokenizingString(math_exp)

    # Displaying TOKENS LIST
    print("LIST of TOKENS -> ", end="")
    for token in tokens_list:
        print(token, end="  ")


if __name__ == "__main__":
    main()
