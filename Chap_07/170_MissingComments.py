"""
The program READS one or more Python Source FILE (whose NAMES is provided as a COMMAND-LINE ARGUMENTS)
and identifies the FUNCTIONS that are NOT immediately preceded by a COMMENT.
After that, it returns the NAMES of these FUNCTIONS along with 
the FILENAME and LINE NUMBER where the definitions of the functions themselves are located.
"""


# The system module must be imported to ACCESS the command-line ARGUMENTS
import sys


try:
    if len(sys.argv) < 2:
        raise Exception

    for i in range(1, len(sys.argv)):
        # Opening the files provided by command-line arguments in reading mode
        f_name_opened = open(sys.argv[i], "r")
        for num_line, line in enumerate(f_name_opened.readlines(), 1):
            if line.strip() == "":
                previous_line = "-"
                continue
            if line.strip()[0:3] == "def" and previous_line.strip()[0] != "#":
                function_name = line.strip()[4:line.strip().index("(")]
                print("function: {} - file: {} - line: {}".format(function_name,
                                                                  sys.argv[i], num_line))
            previous_line = line

        # Closing opened files
        f_name_opened.close()

# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[i]))
    quit()

# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line argument.")
    quit()
