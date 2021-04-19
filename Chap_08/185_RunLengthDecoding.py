"""
The program starting from an ENCODED LIST
returns the same LIST DECODED.
"""


# START Definition of FUNCTION


def decodeList(list_to_decode):
    # BASE CASE
    if list_to_decode == []:
        return []
    # RECURSIVE CASES
    else:
        tmp = []
        for i in range(list_to_decode[1]):
            tmp.append(list_to_decode[0])
        return tmp + decodeList(list_to_decode[2:])


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # LIST TESTING
    all_list_to_decode = [
        ["A", 12, "B", 4, "C", 6, "D", 1],
        ["A", 2, "B", 1, "C", 1, "B", 10],
        ["A", 1, "B", 1, "C", 1, "D", 1],
        ["A", 5, "B", 1, "A", 5, "B", 1],
        ["A", 1, "B", 1],
        ["A", 5],
    ]

    # Computing and displaying the RESULTS
    for list_to_decode in all_list_to_decode:
        print("ORIGINAL ENCODED LIST -> ", end="")
        print(list_to_decode)
        print("DECODED LIST-> ", end="")
        print(decodeList(list_to_decode))


if __name__ == "__main__":
    main()
