"""
The horoscopes commonly reported in newspapers
use the position of the sun at the time of one’s birth to try and predict the future.
This system of astrology divides the year into twelve zodiac signs,
as outline in the table below:

    Zodiac Sign	              Date Range
     Capricorn	        December 22 to January 19
     Aquarius	        January 20 to February 18
      Pisces	         February 19 to March 20
      Aries	               March 21 to April 19
      Taurus	           April 20 to May 20
      Gemini	            May 21 to June 20
      Cancer	           June 21 to July 22
       Leo	               July 23 to August 22
      Virgo	            August 23 to September 22
      Libra	            September 23 to October 22
     Scorpio	         October 23 to November 21
   Sagittarius	        November 22 to December 21

Write a program that asks the user to enter his or her month and day of birth.
Then your program should report the user’s zodiac sign as part of an appropriate output message.
"""

# START Definition of FUNCTIONS


def validaMonth(stringInput):
    month = stringInput.upper()
    if (month == "JANUARY") or (month == "FEBRUARY") or (month == "MARCH") or \
        (month == "APRIL") or (month == "MAY") or (month == "JUNE") or \
        (month == "JULY") or (month == "AUGUST") or (month == "SEPTEMBER") or \
            (month == "OCTOBER") or (month == "NOVEMBER") or (month == "DECEMBER"):
        return True
    else:
        return False


def valutaIntValido(numero):
    if numero.isdigit():
        if 0 < int(numero) <= 31:    # Possible evolution: 28/30/31 days
            return True
    return False


def dateToZodiacSign(month, day):     # Possible evolution: IF NESTED (if same month)
    month = month.upper()
    if (month == "DECEMBER" and day >= 22) or (month == "JANUARY" and day <= 19):
        return "CAPRICORN"
    elif (month == "JANUARY" and day >= 20) or (month == "FEBRUARY" and day <= 18):
        return "AQUARIUS"
    elif (month == "FEBRUARY" and day >= 19) or (month == "MARCH" and day <= 20):
        return "PISCES"
    elif (month == "MARCH" and day >= 21) or (month == "APRIL" and day <= 19):
        return "ARIES"
    elif (month == "APRIL" and day >= 20) or (month == "MAY" and day <= 20):
        return "TAURUS"
    elif (month == "MAY" and day >= 21) or (month == "JUNE" and day <= 20):
        return "GEMINI"
    elif (month == "JUNE" and day >= 21) or (month == "JULY" and day <= 22):
        return "CANCER"
    elif (month == "JULY" and day >= 23) or (month == "AUGUST" and day <= 22):
        return "LEO"
    elif (month == "AUGUST" and day >= 23) or (month == "SEPTEMBER" and day <= 22):
        return "VIRGO"
    elif (month == "SEPTEMBER" and day >= 23) or (month == "OCTOBER" and day <= 22):
        return "LIBRA"
    elif (month == "OCTOBER" and day >= 23) or (month == "NOVEMBER" and day <= 21):
        return "SCORPIO"
    else:
        return "SAGITTARIUS"    # 22 November -> 21 December


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
print("Enter your MONTH and DAY of BIRTH.")
month = input("MONTH: ")
day = input("DAY: ")
monthValidated = validaMonth(month)
dayIntValidated = valutaIntValido(day)

while not(monthValidated and dayIntValidated):
    print("Incorrect entry. Try again.")
    print("Enter your MONTH and DAY of BIRTH.")
    month = input("MONTH: ")
    day = input("DAY: ")
    monthValidated = validaMonth(month)
    dayIntValidated = valutaIntValido(day)


# Conversion STR -> INT
day = int(day)


# Evaluation DATE -> ZODIAC SIGN
zodiacSign = dateToZodiacSign(month, day)


# Displaying the RESULTS
print("Your ZODIAC SIGN is " + zodiacSign +
      " (date of birth " + month.upper() + " " + str(day) + ").")
