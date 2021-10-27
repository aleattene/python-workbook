"""
The program, using the TOKENIZING process,
converts a STRING entered by the USER in a LIST of SUBSTRINGS (TOKENS), 
also identifying the UNARY (u+ or u-) and BINARY operators.
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
        if string[i] in tokens:
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
            tokens_list.append(tmp)
        i += 1
    return tokens_list      # RETURN LIST of TOKENS


def operatorUnaryBinary(original_tokens_list):
    tokens_list = original_tokens_list[:]   # copy list
    operators = ["+", "-"]
    if tokens_list[0] in operators:
        # duplicates accepted
        tokens_list[0] = "u" + tokens_list[0]
    for i in range(1, len(tokens_list)):
        if tokens_list[i] in operators and tokens_list[i-1] == "(":
            # duplicates accepted
            tokens_list[i] = "u" + tokens_list[i]
    return tokens_list


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition of DATA entered by the USER
    math_exp = input("Enter the MATHEMATICAL EXPRESSION: ")
    # STRING TESTING
    # math_exp = "-1*(-2 + (6 * (3-1)) / 844 + (74 - (-3)) / 121-10+10"

    # Generation of the TOKENS LIST
    tokens_list = tokenizingString(math_exp)

    # Generation of the TOKENS LIST with the identification of UNARY and BINARY operators
    tokens_list_updated = operatorUnaryBinary(tokens_list)

    # Displaying TOKENS LIST
    print("LIST of TOKENS -> ", end="")
    for token in tokens_list_updated:
        print(token, end="  ")


if __name__ == "__main__":
    main()
