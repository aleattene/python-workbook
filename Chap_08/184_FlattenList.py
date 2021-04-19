"""
The program starting from a LIST of NESTED LIST
returns the same LIST FLATTENED.
"""


# START Definition of FUNCTION


def flattenList(list_to_flatten):
    # BASE CASE
    if list_to_flatten == []:
        return []
    # RECURSIVE CASES
    if type(list_to_flatten[0]) is list:
        l1 = flattenList(list_to_flatten[0])
        l2 = flattenList(list_to_flatten[1:])
        return l1 + l2
    else:
        l1 = [list_to_flatten[0]]
        l2 = flattenList(list_to_flatten[1:])
        return l1 + l2


# END Definition of FUNCTION


# START MAIN PROGRAM
def main():

    # LIST TESTING
    all_list_to_flatten = [
        [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]],
        [1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]]],
        [1, [2, 3], [4, 5], [6, 7], [8, 9], [10]],
        [[1], [2], [3], [4], 5, 6, [7], [8], [9], [10]],
        [0],
        []
    ]

    # Computing and displaying the RESULTS
    for list_to_flatten in all_list_to_flatten:
        print("ORIGINAL LIST -> ", end="")
        print(list_to_flatten)
        print("FLATTENED LIST -> ", end="")
        print(flattenList(list_to_flatten))


if __name__ == "__main__":
    main()
