"""
The program displays the FIRST 10 lines of a FILE
whose NAME is provided as a COMMAND-LINE ARGUMENT, 
CATCHING and HANDLING any EXCEPTIONS.
"""

# The system module must be imported to ACCESS the command-line ARGUMENTS
import sys

# Declaration of the CONSTANTS
NUM_LINES = 10

try:
    if len(sys.argv) != 2:
        raise Exception
    # Opening the file name (sysargv[1]) in read mode
    with open(sys.argv[1], "r") as f_name_opened:
        # Reading and displaying the first 10 lines of the opened file
        print("************************************* " +
              "FIRST 10 LINES of the FILE \"{}\"".format(sys.argv[1]) +
              " *************************************")
        for i in range(NUM_LINES):
            print(f_name_opened.readline().rstrip().encode(
                "latin-1").decode("utf-8"))
# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[1]))
    quit()
# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line argument.")
    quit()
