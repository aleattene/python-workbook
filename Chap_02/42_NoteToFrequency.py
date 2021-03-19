"""
The Program receives from the USER the NAME of a MUSICAL note (for example C1, B2, etc) 
and displaying its frequency.
"""

# START Definition of FUNCTIONS


def noteValida(note):
    if len(note) == 2:
        if 65 <= ord(note[0].upper()) <= 71:
            if 48 <= ord(note[1]) <= 56:
                return True
    return False


def noteToFrequency(note):
    if note[0].upper() == "C":
        frequency = 261.63 * (2 ** (int(note[1])-4))
    elif note[0].upper() == "D":
        frequency = 293.66 * (2 ** (int(note[1])-4))
    elif note[0].upper() == "E":
        frequency = 329.63 * (2 ** (int(note[1])-4))
    elif note[0].upper() == "F":
        frequency = 349.23 * (2 ** (int(note[1])-4))
    elif note[0].upper() == "G":
        frequency = 392.00 * (2 ** (int(note[1])-4))
    elif note[0].upper() == "A":
        frequency = 440.00 * (2 ** (int(note[1])-4))
    elif note[0].upper() == "B":
        frequency = 493.88 * (2 ** (int(note[1])-4))
    return frequency


# END Definition of FUNCTION


# Acquisition and Control of the DATA entered by the USER
note = input("Enter the NOTE (C0, B4, D2, etc): ")
noteValidated = noteValida(note)

while not(noteValidated):
    print("Incorrect entry. Try again.")
    note = input("Enter the NOTE (C0, B4, D2, etc): ")
    noteValidated = noteValida(note)


# Identification Note -> Frequency
frequencyNote = noteToFrequency(note)


# Displaying the RESULT (float formatted with two decimal digits after comma)
print("The FREQUENCY of the NOTE \"" + note.upper() +
      "\" is %.2f" % frequencyNote + " Hz")
