""" 
The Program receives from the USER the QUANTITY of WATER 
of which you must INCREASE the TEMPERATURE 
from a initial TEMPERATURE T1 to a final TEMPERATURE T2 
and computes the AMOUNT of ENERGY required for this VARIATION THERMIC.
REFERENCE EQUATION:  q = m * C * (T2 - T1)
"""

# Start Definition of FUNCTIONS


def valutaFloat(numero):
    if numero.isdigit():
        countPoints = 0
        for char in numero:
            if ord(char) == 46:
                countPoints += 1
        if countPoints == 1 and numero != ".":
            if isinstance(float(numero), float):
                return True
    return False


def valutaStatoLiquido(temperatura):
    if valutaFloat(temperatura) or temperatura.isdigit():
        temperatura = int(temperatura)
        if 0 < temperatura < 100:
            return True
    return False


# End Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
massWater = input("Enter the MASS of Water (grams or milliliters): ")
tempInitial = input("Enter the INITIAL Temperature (1-99 degrees Celsius): ")
tempFinal = input("Enter the FINAL Temperature (1-99 degrees Celsius): ")

while not(valutaStatoLiquido(tempInitial) and (valutaStatoLiquido(tempFinal))) or \
        not(massWater.isdigit() and massWater != "0"):
    print("Incorrect entry. Try again.")
    massWater = input("Enter the MASS of Water (grams or milliliters): ")
    tempInitial = input(
        "Enter the INITIAL Temperature (1-99 degrees Celsius): ")
    tempFinal = input("Enter the FINAL Temperature (1-99 degrees Celsius): ")

# Conversion STR -> FLOAT
deltaT = float(tempFinal) - float(tempInitial)
massWater = float(massWater)

# Computing the ENERGY EXPENDITURE and energy COSTS
qEnergyJ = massWater * 4.186 * deltaT    # C Water = 4.186 J / g °C
qEnergyKwh = qEnergyJ / (3.6 * 10 ** 6)  # 1 Kwh = 3.6 * (10 ** 6) Joule
costEnergy = abs(qEnergyKwh) * 8.9       # Energy Cost = 8.9 cents for kwh

# Displaying the RESULTS
if qEnergyJ > 0:
    print("Amount of ENERGY that must be ADDED to achieve the desidered TEMPERATURE CHANGE = %.2f"
          % qEnergyJ + " Joule / %.6f" % qEnergyKwh + " Kwh")
    print("COST of HEATING the Water = %.4f" % costEnergy + " cents")
elif qEnergyJ < 0:
    print("Amount of ENERGY that must be REMOVED to achieve the desidered TEMPERATURE CHANGE = %.2f"
          % abs(qEnergyJ) + " Joule / %.6f" % abs(qEnergyKwh) + " Kwh")
    print("COST of COOLING the Water = %.4f" % costEnergy + " cents")
else:
    print("NO TEMPERATURE CHANGE.")
