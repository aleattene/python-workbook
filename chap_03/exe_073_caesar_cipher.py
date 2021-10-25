"""
The program receives a MESSAGE from the USER 
and returns (displaying it) the same MESSAGE, 
ENCODED (or DECODED) using the CAESAR CIPHER.
"""


# START Definition of FUNCTIONS


def valutaInteger(numero):
    if len(numero) > 1:
        if numero.isdigit() or \
                (numero[0] == "-" and numero[1] != "0" and numero[1:].isdigit()):
            return True
    else:
        if numero.isdigit():
            return True
    return False


def caesarCipher(message, shift):
    message_out = ""
    ALPHABET = 26
    if shift > ALPHABET:
        shift = shift % ALPHABET
    for i in range(len(message)):
        if "A" <= message[i] <= "Z":
            char_shifted = (ord(message[i])+shift)
            if char_shifted > 90:
                message_out += chr(char_shifted-ALPHABET)
            elif char_shifted < 65:
                message_out += chr(char_shifted+ALPHABET)
            else:
                message_out += chr(char_shifted)
        elif "a" <= message[i] <= "z":
            char_shifted = (ord(message[i])+shift)
            if char_shifted > 122:
                message_out += chr(char_shifted-ALPHABET)
            elif char_shifted < 97:
                message_out += chr(char_shifted+ALPHABET)
            else:
                message_out += chr(char_shifted)
        else:
            message_out += message[i]
    return message_out


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
message_in = input("Enter the MESSAGGE: ")

shift = input("Enter the SHIFT amount to apply at the previous message: ")
shift_validated = valutaInteger(shift)

while not(shift_validated):
    print("Incorrect entry. Try again.")
    shift = input("Enter the SHIFT amount to apply at the previous message: ")
    shift_validated = valutaInteger(shift)


# ENCODING or DECODING of the MESSAGE
message_out = caesarCipher(message_in, int(shift))


# Displaying the RESULTS
if int(shift) > 0:
    print("ENCODED Message -> " + message_out)
elif int(shift) < 0:
    print("DECODED Message -> " + message_out)
else:
    print("ORIGINAL Message -> " + message_out)
