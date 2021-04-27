"""
The program replaces all sensitive words presents in a text file, 
with asterisks, and rewrites everything in a new file.
The names of the original text file, sensitive words file, 
and the redacted file are provided by the user.
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


# Acquisition and Control of the DATA entered by the USER
while True:
    try:
        # TESTING
        # file_to_read = "wargames_eng.txt"
        # file_sensitive_words = "sensitive_words.txt"
        # file_to_write = "wargames_redacted.txt"
        # Original Text File
        file_to_read = input("Enter the file name to be analyzed: ")
        # Opening the original text file in reading mode
        f_name_read_opened = open(file_to_read, "r")
        # File with the sensitive words
        file_sensitive_words = input("Enter the Sensivite Words file name: ")
        # Opening the file with the sensitive words in reading mode
        f_name_sensitive_words_opened = open(file_sensitive_words, "r")
        # Redacted Text File
        file_to_write = input(
            "Enter the file name that will be created for the text redacted: ")
        # Opening or Creating Redacted Text File in write mode
        f_name_write_opened = open(file_to_write, "w")
        break
    # Exception Type -> File not found
    except FileNotFoundError:
        print("Warning, one or more files entered were not found.")
        # Possible evolution -> handle exception for each file inserted

# List that will contain all sensitive words
sensitive_words = []
for word in f_name_sensitive_words_opened.readlines():
    sensitive_words.append(word.strip().lower())


# Select and redacts each Line returned from the readlines method
for line in f_name_read_opened.readlines():
    for word in sensitive_words:
        if word in line.lower():
            # replacing the sensitive word with asterisks
            line = line.lower().replace(word, "*" * len(word))
    # writing the redacted line to the new file
    f_name_write_opened.write(line)


# Closing opened files
f_name_read_opened.close()
f_name_sensitive_words_opened.close()
f_name_write_opened.close()


# Opening and reading of the previously written file
with open(file_to_write, "r") as file_written:
    print(file_written.read())
# possible evolution -> handle encoding/decoding and capitalization
