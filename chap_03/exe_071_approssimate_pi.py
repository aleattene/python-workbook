"""
The program DISPLAYS the first 15 APPROXIMATIONS of PI.
"""


# Declaration of VARIABLES
pi = 3
n = 2
approssimation = 0


# Displaying the HEADER
print("***************************************************")
print("|    LIST of the first 15 APPROXIMATIONS of PI    |")
print("***************************************************")


# Computing of the first 15 APPROXIMATIONS of PI
while approssimation != 15:
    nextTerm = 4 / (n * (n + 1) * (n + 2))
    if approssimation % 2 == 0:
        pi = pi + nextTerm
        # Displaying the PROGRESSIVE RESULT
        print("|%16s" % "" + "%.15f" % pi + "%16s!" % "")
        n += 2
        approssimation += 1
    else:
        pi = pi - nextTerm
        # Displaying the PROGRESSIVE RESULT
        print("!%16s" % "" + "%.15f" % pi + "%16s!" % "")
        n += 2
        approssimation += 1


# Displaying the FOOTER
print("***************************************************")
