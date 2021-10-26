"""
In a particular jurisdiction, taxi fares consist of a base fare of €4.00,
plus €0.25 for every 140 meters travelled.
Write a function that takes the distance travelled (in kilometers) as its only parameter and
returns the total fare as its only result.
Write a main program that demonstrates the function.
"""


# START Definition of FUNCTIONS


def valutaEntry(number):
    # Check Entry -> INT or FLOAT POSITIVE
    return True


def computesTaxiFare(distance):
    BASE_FARE = 4.00                    # BASE FARE = $4.00
    VARIABLE_FARE = 0.25                # $0.25 every 140 mt
    distance_m = distance * 1000        # conversion km -> m
    distance_140m = distance_m / 140
    taxi_fare = BASE_FARE + (distance_140m * VARIABLE_FARE)
    return taxi_fare


# END Definition of FUNCTIONS


# Acquisition and Control of the DATA entered by the USER
distance_km = input("Enter the DISTANCE TRAVELLED (kilometers): ")
distance_km_validated = valutaEntry(distance_km)

while not(distance_km_validated):
    print("Incorrect entry. Try again.")
    distance_km = input("Enter the DISTANCE TRAVELLED (kilometers): ")
    distance_km_validated = valutaEntry(distance_km)


# DISTANCE conversion : STR -> FLOAT
distance_km = float(distance_km)


# TAXI FARE computing
taxi_fare = computesTaxiFare(distance_km)


# Displaying the RESULT
print("For %.2f" % distance_km + " km travelled the TAXI FARE is $ %.2f" % taxi_fare + ".")
