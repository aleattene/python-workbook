"""
Many recipe books still use cups, tablespoons and teaspoons
to describe the volumes of ingredients used when cooking or baking.
While such recipes are easy enough to follow if you have the appropriate measuring cups and spoons,
they can be difficult to double, triple or quadruple when cooking Christmas dinner for the entire extended family.
For example, a recipe that calls for 4 tablespoons of an ingredient requires 16 tablespoons when quadrupled.
However, 16 tablespoons would be better expressed (and easier to measure) as 1 cup.
Write a function that expresses an imperial volume using the largest units possible.
The function will take the number of units as its first parameter, and
the unit of measure (cup, tablespoon or teaspoon) as its second parameter.
It will return a string representing the measure using the largest possible units as its only result.
For example, if the function is provided with parameters representing 59 teaspoons then
it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.
"""


# START Definition of the FUNCTIONS


def checkUnits(number):
    if number.isdigit():
        if int(number) > 0:
            return True
    return False


def checkUnityMeasure(number):
    if number.isdigit():
        if 1 <= int(number) <= 3:
            return True
    return False


def unityMeasureDescription(value, unity_measure):
    if unity_measure == "1":
        if int(value) == 1:
            return "teaspoon"
        else:
            return "teaspoons"
    elif unity_measure == "2":
        if int(value) == 1:
            return "tablespoon"
        else:
            return "tablespoons"
    elif unity_measure == "3":
        if int(value) == 1:
            return "cup"
        else:
            return "cups"


def reduceMeasures(units, unity_measure):       # Possible evolution -> REFACTORING
    units = int(units)
    cups = 0
    tablespoons = 0
    teaspoons = 0
    if unity_measure == "3":
        cups = units
    elif unity_measure == "2":
        if units < 16:
            tablespoons = units
        else:
            cups = units // 16
            tablespoons = units % 16
    else:    # unity_meaasure == "1":
        if units < 48:
            tablespoons = units // 3
            teaspoons = units % 3
        else:
            cups = units // 48
            tablespoons = units % 48
            teaspoons = tablespoons % 3
            tablespoons = tablespoons // 3
    cups_reduced = "{} {}".format(
        cups, unityMeasureDescription(cups, "3"))
    tablespoons_reduced = "{} {}".format(
        tablespoons, unityMeasureDescription(tablespoons, "2"))
    teaspoons_reduced = "{} {}".format(
        teaspoons, unityMeasureDescription(teaspoons, "1"))
    return "{} + {} + {}".format(cups_reduced, tablespoons_reduced, teaspoons_reduced)


# END Definition of FUNCTIONS


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the DATA entered by the USER
    print("Enter the UNITS NUMBER of the VOLUME and the UNITY of MEASURE.")
    units = input("Number of UNITS: ")
    unity_measure = input(
        "UNIT of MEASURE (cup(3),tablespoon(2),teaspoon(1)): ")
    units_checked = checkUnits(units)
    unity_measure_checked = checkUnityMeasure(unity_measure)

    while not(units_checked and unity_measure_checked):
        print("Incorrect entry. Try again.")
        print("Enter the UNITS NUMBER of the VOLUME and the UNITY of MEASURE.")
        units = input("Number of UNITS: ")
        unity_measure = input(
            "UNIT of MEASURE (cup(3),tablespoon(2),teaspoon(1)): ")
        units_checked = checkUnits(units)
        unity_measure_checked = checkUnityMeasure(unity_measure)

    # Displaying the RESULTS
    print("FINAL RESULT -> {} {} = ".format
          (units, unityMeasureDescription(units, unity_measure)), end="")
    print("{}".format(reduceMeasures(units, unity_measure)))


if __name__ == "__main__":
    main()
