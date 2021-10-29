"""
The program receives a WORD from the USER 
and determines whether or not 
it CAN BE SPELLED using ONLY the SYMBOLS of the chemical elements.
"""

# DICTIONARY of the CHEMICAL ELEMENTS
elements_dictionary = {
    "H": "Hydrogen", "He": "Helium", "Li": "Lithium", "Be": "Beryllium",
    "B": "Boron", "C": "Carbon", "N": "Nitrogen", "O": "Oxygen",
    "F": "Fluorine", "Ne": "Neon", "Na": "Sodium", "Mg": "Magnesium",
    "Al": "Aluminium", "Si": "Silicon", "P": "Phosphorus", "S": "Sulfur",
    "Cl": "Chlorine", "Ar": "Argon", "K": "Potassium", "Ca": "Calcium",
    "Sc": "Scandium", "Ti": "Titanium", "V": "Vanadium", "Cr": "Chromium",
    "Mn": "Manganese", "Fe": "Iron", "Co": "Cobalt", "Ni": "Nickel",
    "Cu": "Copper", "Zn": "Zinc", "Ga": "Gallium", "Ge": "Germanium",
    "As": "Arsenic", "Se": "Selenium", "Br": "Bromine", "Kr": "Krypton",
    "Rb": "Rubidium", "Sr": "Strontium", "Y": "Yttrium", "Zr": "Zirconium",
    "Nb": "Niobium", "Mo": "Molybdenum", "Tc": "Technetium", "Ru": "Ruthenium",
    "Rh": "Rhodium", "Pd": "Palladium", "Ag": "Silver", "Cd": "Cadmium",
    "In": "Indium", "Sn": "Tin", "Sb": "Antimony", "Te": "Tellurium",
    "I": "Iodine", "Xe": "Xenon", "Cs": "Caesium", "Ba": "Barium",
    "La": "Lanthanum", "Ce": "Cerium", "Pr": "Praseodymium", "Nd": "Neodymium",
    "Pm": "Promethium", "Sm": "Samarium", "Eu": "Europium", "Gd": "Gadolinium",
    "Tb": "Terbium", "Dy": "Dysprosium", "Ho": "Holmium", "Er": "Erbium",
    "Tm": "Thulium", "Yb": "Ytterbium", "Lu": "Lutetium", "Hf": "Hafnium",
    "Ta": "Tantalum", "W": "Tungsten", "Re": "Rhenium", "Os": "Osmium",
    "Ir": "Iridium", "Pt": "Platinum", "Au": "Gold", "Hg": "Mercury",
    "Tl": "Thallium", "Pb": "Lead", "Bi": "Bismuth", "Po": "Polonium",
    "At": "Astatine", "Rn": "Radon", "Fr": "Francium", "Ra": "Radium",
    "Ac": "Actinium", "Th": "Thorium", "Pa": "Protactinium", "U": "Uranium",
    "Np": "Neptunium", "Pu": "Plutonium", "Am": "Americium", "Cm": "Curium",
    "Bk": "Berkelium", "Cf": "Californium", "Es": "Einsteinium",
    "Fm": "Fermium", "Md": "Mendelevium", "No": "Nobelium", "Lr": "Lawrencium",
    "Rf": "Rutherfordium", "Db": "Dubnium", "Sg": "Seaborgium", "Bh": "Bohrium",
    "Hs": "Hassium", "Mt": "Meitnerium", "Ds": "Darmstadtium", "Rg": "Roentgenium",
    "Cn": "Copernicium", "Uut": "Ununtrium", "Fl": "Flerovium", "Uup": "Ununpentium",
    "Lv": "Livermorium", "Uus": "Ununseptium", "Uuo": "ununoctium"
}

# LIST of the CHEMICAL ELEMENTS
elements_list = elements_dictionary.keys()


# START Definition of the RECURSIVE FUNCTION


def spellingElementSymbols(word, elements_list):
    if len(word) == 0:
        return ""
    else:
        if len(word) > 2:
            if word[0:3].capitalize() in elements_list:
                return word[0:3].capitalize() + spellingElementSymbols(word[3:len(word)], elements_list)
        if len(word) > 1:
            if word[0:2].capitalize() in elements_list:
                return word[0:2].capitalize() + spellingElementSymbols(word[2:len(word)], elements_list)
        if len(word) > 0:
            if word[0].capitalize() in elements_list:
                return word[0].capitalize() + spellingElementSymbols(word[1:len(word)], elements_list)
        return "" + spellingElementSymbols("", elements_list)


# END Definition of the RECURSIVE FUNCTION


# START MAIN PROGRAM
def main():

    # Acquisition of the WORD entered by the USER
    word = input("Enter a WORD: ")

    # Evaluation of the word:
    # -> whether or not it can be spelled using only the symbols of the chemical elements
    spelling_word = spellingElementSymbols(word, elements_list)

    # Displaying the RESULT
    if len(spelling_word) == len(word) and len(word) != 0:
        print("The word \"{}\" CAN BE SPELLED using the symbols of the chemical elements as \"{}\".".format(
            word, spelling_word))
    else:
        print("The word \"{}\" CANNOT BE SPELLED with any combination ".format(word) +
              "of the symbols of the chemical elements.")


if __name__ == "__main__":
    main()
