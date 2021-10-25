"""
One of the first known examples of encryption was used by Julius Caesar.
Caesar needed to provide written instructions to his generals,
but he didn’t want his enemies to learn his plans if the message slipped into their hands.
As a result, he developed what later became known as the Caesar cipher.
The idea behind this cipher is simple
(and as such, it provides no protection against modern code breaking techniques).
Each letter in the original message is shifted by 3 places.
As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.

The last three letters in the alphabet are wrapped around to the beginning:
- X becomes A,
- Y becomes B and
- Z becomes C.

Non-letter characters are not modified by the cipher.

Write a program that implements a Caesar cipher.
Allow the user to supply the message and the shift amount,
and then display the shifted message.

Ensure that your program encodes both uppercase and lowercase letters.
Your program should also support negative shift values
so that it can be used both to encode messages and decode messages.
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
