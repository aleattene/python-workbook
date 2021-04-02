"""
The program receives a MATHEMATICAL OPERATOR from the USER
and returns (displaying it) its EXECUTION PRIORITY.
"""


# START Definition of the FUNCTIONS


def operatorPrecedence(operator):
    if len(operator) == 1:
        if (operator == "+" or operator == "-"):
            return 1
        elif (operator == "*" or operator == "/"):
            return 2
        elif (operator == "^"):
            return 3
    return -1


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # DATA acquisition (from USER)
    operator = input(
        "Enter the MATHEMATICAL OPERATOR ( (+) (-) (*) (/) (^) ): ")

    # Evaluation of the EXECUTION PRIORITY of the MATHEMATICAL OPERATOR entered
    operator_priority = operatorPrecedence(operator)
    if operator_priority == 1:
        priority = "low"
    elif operator_priority == 2:
        priority = "middle"
    elif operator_priority == 3:
        priority = "high"

    # Displaying the RESULTS
    if 1 <= operator_priority <= 3:
        print("The MATHEMATICAL OPERATOR ({}) ".format(operator) +
              "has EXECUTION PRIORITY {} out of 3 ({} priority).".format(operator_priority, priority))
    elif operator_priority == -1:
        print("WARNING. NO VALID mathematical OPERATOR has been ENTERED.")


if __name__ == "__main__":
    main()
