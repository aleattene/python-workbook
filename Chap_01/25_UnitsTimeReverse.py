"""
The Program receives from the USER a PERIOD of TIME expressed in seconds
and returns it in the format  D:HH:MM:SS
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
    days = int(seconds / 86400)
    seconds = seconds % 86400
if seconds >= 3600:
    hours = int(seconds / 3600)
    seconds = seconds % 3600
if seconds >= 60:
    minutes = int(seconds / 60)
    seconds = seconds % 60

# Formatting TIME PERIOD (conversion INT -> STR)  - Possible Alternative -> %02d
days = str(days)
hours = formatDate(str(hours))
minutes = formatDate(str(minutes))
seconds = formatDate(str(seconds))

# Displaying the RESULTS
print("DURATION entered -> " + days + ":" + hours +
      ":" + minutes + ":" + seconds + " (D:HH:MM:SS)")
