"""
The program receives a WORD from the USER
and constructs a SEQUENCE of CHEMICAL ELEMENTS.
"""

# DICTIONARY of the CHEMICAL ELEMENTS
chemical_elements_list = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen",
    "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus", "Sulfur",
    "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium",
    "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic",
    "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
    "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver",
    "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium",
    "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium",
    "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium",
    "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold",
    "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium",
    "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium",
    "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium",
    "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium",
    "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Ununtrium", "Flerovium",
    "Ununpentium", "Livermorium", "Ununseptium", "Ununoctium"
]


# START Definition of the RECURSIVE FUNCTION


def generateSequence(word, chemical_elements_list):
    # BASE CASE
    if word == "":
        return []
    # RECURSIVE CASES
    else:
        # REMOVAL of the WORD from list (already present in sequence)
        chemical_elements_list.remove(word)
        # CANDIDATE WORDS present within the updated list
        selected_words = []
        for i in range(len(chemical_elements_list)):
            if word[-1].upper() == chemical_elements_list[i][0]:
                selected_words.append(chemical_elements_list[i])
        # Selection of the LONGEST WORD among those candidates
        sequence = []
        if len(selected_words) > 1:
            for s in range(len(selected_words)-1):
                # Previous word longer than next word
                if len(selected_words[s]) > len(selected_words[s+1]):
                    if sequence == []:
                        sequence.append(selected_words[s])
                    else:
                        sequence[0] = selected_words[s]
                # Previous word shorter or equal than next word
                else:
                    if sequence == []:
                        sequence.append(selected_words[s+1])
                    else:
                        sequence[0] = selected_words[s+1]
        # Only ONE candidate word
        elif len(selected_words) == 1:
            sequence.append(selected_words[0])
        # NO candidate words
        else:
            sequence.append("")
        return sequence + generateSequence(sequence[0], chemical_elements_list)


# END Definition of the RECURSIVE FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition and Control of the WORD entered by the USER
    while True:
        word = input("Enter a WORD: ")
        if word in chemical_elements_list:
            break

    # Generation of WORDS SEQUENCE
    sequence = generateSequence(word, chemical_elements_list)

    # Displaying of the WORDS SEQUENCE
    print("ENTERED WORD -> {}".format(word))
    print("SEQUENCE GENERATED -> {}  ".format(word), end="")
    for element in sequence:
        print(element, end="  ")


if __name__ == "__main__":
    main()
