""" 
The Program receives from the USER a PERIOD of TIME expressed in 
DAYS, HOURS, MINUTES and SECONDS and returns it
expressed in SECONDS.
"""

# START Definition of FUNCTION

def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0":
            return True
    return False

# END Definition of FUNCTION


# Acquisition and Control of the DATA entered by the USER
print("Enter the Duration (days, hours, minutes and seconds).")
days = input("Days: ")
hours = input("Hours: ")
minutes = input("Minutes: ")
seconds = input("Seconds: ")

daysIntPositive = valutaIntPositive(days)
hoursIntPositive = valutaIntPositive(hours)
minutesIntPositive = valutaIntPositive(minutes)
secondsIntPositive = valutaIntPositive(seconds)


while not(daysIntPositive and hoursIntPositive and minutesIntPositive and secondsIntPositive):
    print("Incorrect entry. Try again.")
    print("Enter the Duration (days, hours, minutes and seconds).")
    days = input("Days: ")
    hours = input("Hours: ")
    minutes = input("Minutes: ")
    seconds = input("Seconds: ")

    daysIntPositive = valutaIntPositive(days)
    hoursIntPositive = valutaIntPositive(hours)
    minutesIntPositive = valutaIntPositive(minutes)
    secondsIntPositive = valutaIntPositive(seconds)


# Conversion STR -> INT
days = int(days)
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)


# TIME Computing (seconds)
secondsMinutes = minutes * 60
secondsHours = hours * (60 * 60)
secondsDays = days * (60 * 60 * 24)
duration = seconds + secondsMinutes + secondsHours + secondsDays


# Displaying the RESULT
print("DURATION entered = %i" % duration + " seconds")
