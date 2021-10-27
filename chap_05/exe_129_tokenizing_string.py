"""
Tokenizing is the process of converting a string into a list of substrings, known as tokens.
In many circumstances, a list of tokens is far easier to work with than the original string
because the original string may have irregular spacing.
In some cases substantial work is also required to determine where one token ends and the next one begins.
In a mathematical expression, tokens are items such as operators, numbers and parentheses.
The operator symbols that we will consider in this (and subsequent) problems are *, /, ˆ, - and +.
Operators and parentheses are easy to identify because the token is always a single character, and
the character is never part of another token.
Numbers are slightly more challenging to identify because the token may consist of multiple characters.
Any sequence of consecutive digits should be treated as one number token.

Write a function that takes a string containing a mathematical expression as its only parameter and
breaks it into a list of tokens.
Each token should be a parenthesis, an operator, or a number
(For simplicity we will only work with integers in this problem).

Return the list of tokens as the function’s only result.

You may assume that the string passed to your function always contains a valid mathematical expression
consisting of parentheses, operators and integers.
However, your function must handle variable amounts of whitespace (including no whitespace) between these elements. Include a main program that demonstrates your tokenizing function by reading an expression from the user and printing the list of tokens. Ensure that the main program will not run when the file containing your solution is imported into another program.
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
        if string[i] in tokens and string[i] not in tokens_list:  # duplicates not accepted
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
            if tmp not in tokens_list:  # duplicates not accepted
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
