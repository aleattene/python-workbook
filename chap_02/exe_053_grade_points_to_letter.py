"""
The Program receives from the USER 
a university EVALUATION in POINTS (for example: 4.0, 3.0, 1.3, etc.)
and returns (displaying it) the corresponding evaluation in LETTERS.
"""

# START Definition of FUNCTIONS


def gradePointsValido(points):
    if len(points) == 1:
        if 48 <= ord(points[0].upper()) <= 52:
            return True
    elif len(points) == 3:
        if (49 <= ord(points[0].upper()) <= 52) and (points[1] == ".") and \
                (points[2] == "0" or points[2] == "3" or points[2] == "7"):
            return True
    return False


def pointsToLetterGrade(points):
    gradePoint = {"4.0": "A+", "4.0": "A", "3.7": "A-", "3.3": "B+",
                  "3.0": "B", "2.7": "B-", "2.3": "C+", "2.0": "C",
                  "1.7": "C-", "1.3": "D+", "1.0": "D", "0": "F"}
    return gradePoint.get(points.upper())


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
points = input("Enter the GRADE POINTS (0, 1.3, 2.7, etc): ")
gradePointsValidated = gradePointsValido(points)

while not(gradePointsValidated):
    print("Incorrect entry. Try again.")
    points = input("Enter the GRADE POINTS (0, 1.3, 2.7, etc): ")
    gradePointsValidated = gradePointsValido(points)


# Identification GRADE POINTS -> LETTER GRADE
letterGrade = pointsToLetterGrade(points)


# Displaying the RESULTS
print("The LETTER GRADE of the grade points \"" + points +
      "\" is " + letterGrade)
