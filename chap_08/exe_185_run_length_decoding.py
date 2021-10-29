"""
Run-length encoding is a simple data compression technique that can be effective
when repeated values occur at adjacent positions within a list.

Compression is achieved by replacing groups of repeated values with one copy of the value,
followed by the number of times that it should be repeated.

For example:
the list ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B","B","A","A","A","A","A","A","B"]
would be compressed as ["A",12,"B",4,"A",6,"B",1].

Decompression is performed by replicating each value in the list the number of times indicated.

Write a recursive function that decompresses a run-length encoded list.
Your recursive function will take a run-length compressed list as its only argument.
It will return the decompressed list as its only result.

Create a main program that displays a run-length encoded list and the result of decoding it.
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
        print("DECODED LIST -> ", end="")
        print(decodeList(list_to_decode))


if __name__ == "__main__":
    main()
