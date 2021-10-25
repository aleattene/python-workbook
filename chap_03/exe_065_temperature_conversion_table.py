"""
The program displays a TEMPERATURE CONVERSION TABLE with:
- degrees CELSIUS,
- degrees FAHRENHEIT,
for all TEMPERATURES between 0 and 100 degrees CELSIUS
that are MULTIPLES of 10 degrees CELSIUS.
"""

# START Definition of FUNCTIONS


def celsiusToFahrenheit(degreesCelsius):
    degreesFahrenheit = (degreesCelsius * 9 / 5) + 32
    return degreesFahrenheit

# END Definition of FUNCTIONS


# Generation and display of the TEMPERATURE CONVERSION TABLE
print("****************************************")
print("|    TEMPERATURE CONVERSION TABLE      |")
print("****************************************")
print("| degrees CELSIUS | degrees FAHRENHEIT |")
print("****************************************")

for i in range(10, 101, 10):
    degreesFahrenheit = celsiusToFahrenheit(i)
    print("|%9s" % i + "°C      | " + "%10s" %
          degreesFahrenheit + "°F       |")
    print("****************************************")
