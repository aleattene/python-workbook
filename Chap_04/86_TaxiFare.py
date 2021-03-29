"""
The program receives from the USER
the DISTANCE TRAVELLED (in kilometers)
and returns (displaying it) the TAXI FARE,
considering:
- BASE fare = $4.00
- VARIABLE fare = $0.25 every 140 meters travelled.
"""


# START Definition of FUNCTIONS


def valutaEntry(number):
    # Check Entry -> INT or FLOAT POSITIVE
    return True


def computesTaxiFare(distance):
    BASE_FARE = 4.00                    # BASE FARE = $4.00
    variable_fare = 0.25                # $0.25 every 140 mt
    distance_m = distance * 1000        # conversion km -> m
    distance_140m = distance_m / 140
    taxi_fare = BASE_FARE + (distance_140m * variable_fare)
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
