"""
The Program receives from the USER
SOME university EVALUATIONS in LETTERS (for example A +, C-, F, etc.) 
and returns (displaying it) the corresponding AVERAGE evaluation in POINTS.
"""


# START Definition of FUNCTIONS


def letterGradeValida(letter):
    if len(letter) == 1:
        if (65 <= ord(letter[0].upper()) <= 68) or (letter[0].upper() == "F"):
            return True
    elif len(letter) == 2:
        if (65 <= ord(letter[0].upper()) <= 68):
            if (letter[1] == "+") or (letter[1] == "-"):
                return True
    return False


def letterGradeToPoints(letter):
    letterGrade = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3,
                   "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7,
                   "D+": 1.3, "D": 1.0, "F": 0}
    return letterGrade.get(letter.upper())


# END Definition of FUNCTIONS


# Declaration of VARIABLES
letterEntered = 0
sumPoints = 0


# Acquisition and Control of the DATA entered by the USER
letter = input("Enter the LETTER GRADE (A, A+, A-, etc): ")
letterGradeValidated = letterGradeValida(letter)

while not(letterGradeValidated):
    print("Incorrect entry. Try again.")
    letter = input("Enter the LETTER GRADE (A, A+, A-, etc): ")
    letterGradeValidated = letterGradeValida(letter)

while letter != "":
    if letterGradeValidated:
        letterEntered +=1
        gradePoints = letterGradeToPoints(letter)
        sumPoints += gradePoints
        letter = input("Enter the LETTER GRADE (A, A+, A-, etc) or EMPTY line to QUIT: ")
        letterGradeValidated = letterGradeValida(letter)
    else:
        print("Incorrect entry. Try again.")
        letter = input("Enter the LETTER GRADE (A, A+, A-, etc) or EMPTY line to QUIT: ")
        letterGradeValidated = letterGradeValida(letter)


# GRADE POINT AVERAGE computing
averagePoints = sumPoints / letterEntered


# Displaying the RESULT
print("The GRADE POINT AVERAGE of LETTER GRADES entered is %.1f" % averagePoints)

