"""
Write a function named reverseLookup that finds all of the keys in a dictionary that map to a specific value.
The function will take the dictionary and the value to search for as its only parameters.
It will return a (possibly empty) list of keys from the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function
as part of your solution to this exercise.
Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple keys, a single key, and no keys.
Ensure that your main program only runs
when the file containing your solution to this exercise has not been imported into another program.
"""


# START Definition of the FUNCTION


def checkEntry(values_string):
    # Possible evolution -> CHECK ENTRY -> FLOAT
    pass


def reverseLookup(weigth_people, weigth):
    # Conversion STR -> INT (possible evolution -> FLOAT)
    weight = int(weigth)
    # List of people with the same weight
    weight_mapped = []
    # Analysis within the dictionary
    for key in weigth_people:
        if weight == weigth_people[key]:
            weight_mapped.append(key)
    return weight_mapped


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # DICTIONARY - People Weight
    weigth_people = {
        "Alessandro": 95,
        "Daniela": 50,
        "Davide ": 47,
        "Gianni": 50,
        "Aldo": 85,
        "Manuela": 50
    }

    # Acquisition of DATA entered by the USER
    weight = input("Enter your WEIGHT (kg): ")

    # WEIGHT MAPPING
    mapping_results = reverseLookup(weigth_people, weight)

    # Displaying the RESULTS
    print("MAPPING RESULTS -> ", end="")
    if len(mapping_results) == 0:
        print("NO ONE has", end=" ")
    elif len(mapping_results) == 1:
        print("{} has".format(mapping_results[0].upper()), end=" ")
    else:
        for k in mapping_results:
            print(k.upper(), end=", ")
        print("have", end=" ")
    print("the SAME WEIGHT as YOU ({} kg).".format(weight))


if __name__ == "__main__":
    main()
