"""
The Program receives one YEAR from the USER and calculates the
DATE of EASTER for that same YEAR (using GREGORIAN ALGORITHM).
"""

# START Definition of FUNCTIONS

def valutaIntPositive(numero):
    if numero.isdigit():
        if numero != "0000":
            return True
    return False

def valutaYear(year):
    if valutaIntPositive:
        if len(year) == 4:
            return True
    return False

def dateEaster(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = ((19 * a) + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + (2 * e) + (2 * i) - h - k) % 7
    m = (a + (11 * h) + (22 * l)) // 451
    month = (h + l - (7 * m) + 114) // 31
    month = formatDate(str(month)) 
    day = ((h + l - (7 * m) + 114) % 31 ) + 1
    day = formatDate(str(day))
    dateEaster = day + "-" + month
    return dateEaster

def formatDate(numero):
    if len(numero) == 1:
        numero = "0" + str(numero)
    else:
        numero = str(numero)
    return numero

# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
year = input("Enter the YEAR you want know the EASTER date: ")
yearValidated = valutaYear(year)

while not(yearValidated):
    print("Incorrect entry. Try again.")
    year = input("Enter the YEAR you want know the EASTER date: ")
    yearValidated = valutaYear(year)


# Conversion STR -> INT
year = int(year)


# EASTER DATE Computing
dateEaster = dateEaster(year)

# Displaying the EASTER DATE
print("EASTER DATE = " + dateEaster + "-" + str(year))
