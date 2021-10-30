"""
The program READS a FILE (whose NAME is provided by the USER)
containing a LIST of WORDS and analyzes if are present WORDS 
that whether or not RESPECTING the RULE "I before E except after C".
"""

# Import STRING module
import string


# START Definition of the FUNCTION


# possible evolution -> import function
def removePunctuationMarks(original_string):
    words_list = original_string.split()
    for i in range(len(words_list)):
        # Initial position of the word
        while (words_list[i][0]) in string.punctuation:
            # New word with the same name as the previous one
            words_list[i] = words_list[i].replace(words_list[i][0], "")
        # Final position of the word
        while (words_list[i][-1]) in string.punctuation:
            # New word with the same name as the previous one
            words_list[i] = words_list[i].replace(words_list[i][-1], "")
    return words_list


# END Definition of the FUNCTION


# Acquisition of the file name by the user
filename = input("Enter the FILE name to be analyzed: ")

open_file = True
while open_file:
    try:
        if filename == "":
            raise Exception
        # Opening the file name in read mode
        f_name_opened = open(filename, "r")
        open_file = False
    # Exception -> file not found
    except FileNotFoundError:
        print("Warning, the file \"{}\" wasn't found.".format(filename))
        filename = input("Enter the FILE name to be analyzed: ")
    # Exception -> empty line
    except:
        print("Warning, NO FILE entered.")
        filename = input("Enter the FILE name to be analyzed: ")


# LISTS which will contain the WORDS that FOLLOW or VIOLATE the RULE "IE-CEI"
words_follow_rule = []
words_violate_rule = []

# Select of the each Line from LIST of the LINES (returned from the readlines)
for line in f_name_opened.readlines():
    # Select of the each WORD from LIST of the Words of each line
    for word in removePunctuationMarks(line):
        # For each character
        for i in range(len(word.upper())):
            if i < (len(word) - 1):
                if word.upper()[i] == "I":
                    if word.upper()[i+1] == "E":
                        # Rule Respected but any repeated values ​​not allowed
                        if word not in words_follow_rule:
                            # Rule Respected
                            words_follow_rule.append(word)
                if word.upper()[i] == "E":
                    if word.upper()[i+1] == "I":
                        if i > 0:
                            if word.upper()[i-1] == "C":
                                # Rule Respected but any repeated values ​​not allowed
                                if word not in words_follow_rule:
                                    # Rule Respected
                                    words_follow_rule.append(word)
                            else:
                                # Rule Violated but any repeated values ​​not allowed
                                if word not in words_violate_rule:
                                    # Rule Violated
                                    words_violate_rule.append(word)
                        else:
                            # Rule Violated but any repeated values ​​not allowed
                            if word not in words_violate_rule:
                                # Rule Violated
                                words_violate_rule.append(word)

# Closing the previously opened file
f_name_opened.close()

# Displaying the RESULTS
print("1) WORDS that FOLLOW the rule \"I befor E except after C\" -> ({}) -> ".format(
    len(words_follow_rule)), end="")
for word in words_follow_rule:
    print(word, end=" ")
print("\n2) WORDS that VIOLATE the rule \"I befor E except after C\" -> ({}) -> ".format(
    len(words_violate_rule)), end="")
for word in words_violate_rule:
    print(word, end=" ")
print("\nPROPORTION -> {} : {}".format(len(words_follow_rule), len(words_violate_rule)))
