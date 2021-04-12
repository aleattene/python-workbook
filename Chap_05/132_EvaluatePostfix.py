"""
The program receives a MATHEMATICAL EXPRESSION from the USER
and returns the same expression EXPRESSED in POSTFIX FORM (RPN).
After that, EVALUATES this second expression and displays its VALUE.
"""


# START Definition of the FUNCTIONS


def checkEntry(math_exp):      # possible evolution -> check entry
    pass


def tokenizingString(string):       # possible evolution -> import
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


def operatorUnaryBinary(original_tokens_list):      # possible evolution -> import
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


def operatorPrecedence(operator):      # fuction updated
    if (operator == "+" or operator == "-"):
        return 1
    elif (operator == "*" or operator == "/"):
        return 2
    elif (operator == "u+" or operator == "u-"):
        return 3
    elif (operator == "^"):
        return 4


def infixToPostfix(list_infix_expression):
    token_operators = ["+", "u+", "-", "u-",
                       "*", "/", "^"]  # without parentheses
    operators = []
    postfix = []
    for token in list_infix_expression:
        # CHECK INTEGER
        if token.isdigit():
            postfix.append(token)
        # CHECK OPERATORS
        if token in token_operators:
            while operators != [] and operators[-1] != "(" and \
                    operatorPrecedence(token) <= operatorPrecedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        # CHECK PARENTHESES
        if token == "(":
            operators.append(token)
        if token == ")":
            while operators[-1] != "(":
                postfix.append(operators.pop())
            operators.remove("(")
    while operators != []:
        postfix.append(operators.pop())
    return postfix


def computePostfix(list_postfix_expression):
    infix_operators = ["+", "-", "*", "/", "^"]
    # EMPTY LIST for VALUE EXPRESSION
    values = []
    for token in list_postfix_expression:
        if token.isdigit():
            values.append(int(token))
        elif token == "u-":
            values.append(-1*(values.pop()))
        elif token in infix_operators:
            # SECOND operand (right)
            right = values.pop()
            # FIRST operand (left)
            left = values.pop()
            # COMPUTING the RESULT of the EXPRESSION
            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left / right
            elif token == "^":
                result = left ** right
            # RESULT EXPRESSION
            values.append(result)
    return values[0]


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():
    # Acquisition of DATA entered by the USER
    math_exp = input("Enter the MATHEMATICAL EXPRESSION: ")
    # STRING TESTING (Expected result = 1424)
    # math_exp = "20 + 15 * (100 -5 ) - 21"
    # STRING TESTING (Expected result = -0.08333333)
    # math_exp = "1 / (2 * (3 - (4 + 5)))"
    # STRING TESTING (Expected result = 100
    # math_exp = "(20 * 10 - (11 * 9)) + 1"
    # STRING TESTING (Expected result = 102
    # math_exp = "(20 * 10 - (11 * 9)) + 1"
    # STRING TESTING (Expected result = 199
    # math_exp = "(10 ^ 2) - (11 * 9) + (-2 * (-11 * 9)) "

    # Generation of the TOKENS LIST
    tokens_list = tokenizingString(math_exp)

    # Generation of the TOKENS LIST with the identification of UNARY and BINARY operators
    tokens_list_updated = operatorUnaryBinary(tokens_list)

    # Generation of the POSTFIX LIST
    postfix_expression = infixToPostfix(tokens_list_updated)

    # Computing the RESULT of the EXPRESSION
    result_expression = computePostfix(postfix_expression)

    # Displaying the RESULTS
    print("ORIGINAL EXPRESSION -> {}".format(math_exp))
    print("POSTFIX EXPRESSION -> ", end="")
    for token in postfix_expression:
        print(token, end=" ")
    print("\nRESULT EXPRESSION -> {}".format(result_expression))


if __name__ == "__main__":
    main()
