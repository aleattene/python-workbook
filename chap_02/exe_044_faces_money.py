"""
The program receives from the USER the DENOMINATION of a BANKNOTE
and displays the NAME of the COUNTRY’S LEADER that appears in it.
"""

# START Definition of FUNCTIONS


def faceInBankonote(denomBanknote):
    if denomBanknote == "$1":
        return "George WASHINGTON"
    elif denomBanknote == "$2":
        return "Thomas JEFFERSON"
    elif denomBanknote == "$5":
        return "Abraham LINCOLN"
    elif denomBanknote == "$10":
        return "Alexander HAMILTON"
    elif denomBanknote == "$20":
        return "Andrew JACKSON"
    elif denomBanknote == "$50":
        return "Ulysse S.GRANT"
    elif denomBanknote == "$100":
        return "Benjamin FRANKLIN"
    else:
        return False


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
denomBankonote = input("Enter the DENOMINATION of a BANKNOTE" +
                       "($1, $2 , $5 , $10 , $20 , $50 or $100): ")
faceBankonote = faceInBankonote(denomBankonote)

while (faceBankonote == False):
    print("Incorrect entry. Try again.")
    denomBankonote = input("Enter the DENOMINATION of a BANKNOTE" +
                           "($1, $2 , $5 , $10 , $20 , $50 or $100): ")
    faceBankonote = faceInBankonote(denomBankonote)


# Displaying the RESULTS
print("The FACE of " + faceBankonote +
      " is represented in the BANKNOTE of " + denomBankonote)
