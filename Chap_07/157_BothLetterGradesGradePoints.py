"""
The Program receives a VALUE from the USER.
First of all, it attempts to CONVERT it
from GRADE POINTS (4.0, 3.0, 1.3, etc.) to LETTER GRADE (A+, C-, F, etc.).
If an exception occurs it attempts also to convert it
from LETTER GRADE (A+, C-, F, etc.) to GRADE POINTS (4.0, 3.0, 1.3, etc.).
Finally, if both conversions fail, displays a MESSAGE of ERROR for the user.
"""

# Definition of the Dictionaries
letter_grades = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0
}

grade_points = {
    4.0: "A+/A", 3.7: "A-", 3.3: "B+",
    3.0: "B", 2.7: "B-", 2.3: "C+", 2.0: "C",
    1.7: "C-", 1.3: "D+", 1.0: "D", 0: "F"
}


# Acquisition and Control of the VALUE entered by the USER
value = input("Enter the VALUE to convert (blank line to quit): ")

while value != "":
    try:
        # Displaying the conversion GRADE POINTS -> LETTER GRADE
        value = float(value)
        # Value present as a key in the dictionary
        if value in grade_points:
            print("GRADE POINTS ({}) -> LETTER GRADE \"{}\"".format(value,
                                                                    grade_points[value]))
        else:
            raise ValueError
        value = input("Enter the VALUE to convert (blank line to quit): ")
    # Exception -> Value Error
    except ValueError:
        # Displaying the conversion LETTER GRADE -> GRADE POINTS
        # Value present as a key in the dictionary
        if value in letter_grades:
            print("LETTER GRADE \"{}\" -> GRADE POINTS ({})".format(value,
                                                                    letter_grades[value]))
            value = input("Enter the VALUE to convert (blank line to quit): ")
        # Value not present in both dictionaries
        else:
            print("Incorrect entry. Try again.")
            value = input("Enter the VALUE to convert (blank line to quit): ")
