""" 
The Program calculates the NUMBER of MOLES of a IDEAL GAS 
in a SCUBA tank:
- containing 12 liters of gas
- at a pressure of 20.000.000 Pascals
- at a temperature of 20 degrees Celsius (68 degrees Fahrenheit)
REFERENCE EQUATION (IDEAL GAS):      p * V = n * R * T 
"""

# Declaration of VARIABLES / CONSTANTS
pressure = 20000000            # Pascals
volume = 12                    # Liters
C_IDEAL = 8.314                # J / mol * K
temperatureCelsius = 20        # Celsius


# Conversion Celsius -> Kelvin (Kelvin = Celsius + 273.15)
temperatureKelvin = temperatureCelsius + 273.15


# Computing of the NUMBER of MOLES
nMoli = (pressure * volume) / (C_IDEAL * temperatureKelvin)


# Displaying the RESULTS
print("Dati INPUT: \n - pressure: %i" % pressure +
      " Pascals\n - volume: %i" % volume + " Liters")
print(" - temperature: 20°C (%.2f" % temperatureKelvin + "°K)")
print("\nNUMBER of MOLES calculated = %.2f" % nMoli)
