"""
In this exercise you will reverse the process described in Exercise 24.
Develop a program that begins by reading a number of seconds from the user.
Then your program should display the equivalent amount of time in the form D:HH:MM:SS,
where D, HH, MM, and SS represent days, hours, minutes and seconds respectively.
The hours, minutes and seconds should all be formatted so that they occupy exactly two digits.
Use your research skills determine what additional character needs
to be included in the format specifier so that leading zeros are used
instead of leading spaces when a number is formatted to a particular width.
"""

# START Definition of FUNCTION


def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False


def formatDate(numero):
    if len(numero) == 1:
        numero = "0" + str(numero)
    else:
        numero = str(numero)
    return numero


# END Definition of FUNCTION


# Acquisition and Control of the DATA entered by the USER
seconds = input("Enter the Duration (seconds): ")
secondsIntPositive = valutaIntPositive(seconds)

while not(secondsIntPositive):
    print("Incorrect entry. Try again.")
    seconds = input("Enter the Duration (seconds): ")
    secondsIntPositive = valutaIntPositive(seconds)


# Conversion STR -> INT
seconds = int(seconds)


# Declaration of VARIABLES
days = 0         # 1 day = ( 60 * 60 * 24 ) seconds
hours = 0        # 1 hour = ( 60 * 60 ) seconds
minutes = 0      # 1 minute = 60 seconds

# Computing of DAYS, HOURS, MINUTES and SECONDS
if seconds >= 86400:
    days = seconds // 86400
    seconds = seconds % 86400
if seconds >= 3600:
    hours = seconds // 3600
    seconds = seconds % 3600
if seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60

# Formatting TIME PERIOD (conversion INT -> STR)  - Possible Alternative -> %02d
days = str(days)
hours = formatDate(str(hours))
minutes = formatDate(str(minutes))
seconds = formatDate(str(seconds))

# Displaying the RESULTS
print(f'DURATION entered -> {days}:{hours}:{minutes}:{seconds} (D:HH:MM:SS)')
