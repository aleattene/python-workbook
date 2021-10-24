"""
The following table lists an octave of music notes,
beginning with middle C, along with their frequencies.

Note    Frequency (Hz)
 C4	        261.63
 D4	        293.66
 E4	        329.63
 F4	        349.23
 G4	        392.00
 A4	        440.00
 B4	        493.88

Begin by writing a program that
reads the name of a note from the user and displays the note’s frequency.
Your program should support all of the notes listed previously.

Once you have your program working correctly for the notes listed previously
you should add support for all of the notes from C0 to C8.
While this could be done by adding many additional cases to your if statement,
such a solution is cumbersome, inelegant and unacceptable for the purposes of this exercise.
Instead, you should exploit the relationship between notes in adjacent octaves.
In particular, the frequency of any note in octave n
is half the frequency of the corresponding note in octave n + 1.
By using this relationship, you should be able to add support
for the additional notes without adding additional cases to your if statement.
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


# END Definition of FUNCTIONS


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
