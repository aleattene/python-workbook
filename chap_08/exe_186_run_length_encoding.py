"""
Write a recursive function that implements the run-length compression technique
described in Run-Lenght Decoding Exercise.

Your function will take a list or a string as its only argument.
It should return the run-length compressed list as its only result.

Include a main program that reads a string from the user, compresses it, and displays the run-length encoded result.

Hint: You may want to include a loop inside the body of your recursive function.
"""


# START Definition of FUNCTION


def encodeList(list_to_encode):
    # BASE CASE
    if list_to_encode == []:
        return []
    elif len(list_to_encode) == 1:
        return [list_to_encode[0], 1]
    # RECURSIVE CASES
    else:
        tmp = []
        tmp.append(list_to_encode[0])
        tmp.append(1)
        i = 1
        while list_to_encode[i] == tmp[0]:
            tmp[1] += 1
            i += 1
            if i == (len(list_to_encode)):
                break
        return tmp + encodeList(list_to_encode[i:len(list_to_encode)])


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # LIST TESTING
    all_list_to_encode = [
        ["A", "A", "A", "A", "A", "A", "B", "B",
            "B", "B", "B", "C", "C", "C", "C", "D"],
        ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D"],
        ["A", "A", "A", "C", "C", "C"],
        ["A", "C", "C", "C"],
        ["A"]
    ]

    # Computing and displaying the RESULTS
    for list_to_encode in all_list_to_encode:
        print("ORIGINAL DECODED LIST -> ", end="")
        print(list_to_encode)
        print("ENCODED LIST -> ", end="")
        print(encodeList(list_to_encode))


if __name__ == "__main__":
    main()
