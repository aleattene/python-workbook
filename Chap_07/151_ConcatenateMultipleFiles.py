"""
The program displays the CONCATENATION of ONE or MORE FILES
whose NAMES are provided as COMMAND-LINE ARGUMENTS, 
CATCHING and HANDLING any EXCEPTIONS.
"""

# The system module must be imported to ACCESS the command-line ARGUMENTS
import sys

try:
    # Check that at least one file name was provided as a command-line arguments
    if len(sys.argv) < 2:
        raise Exception
    # For each file name provided as a command-line arguments
    for i in range(1, len(sys.argv)):
        # Opening the file in read mode
        with open(sys.argv[i], "r") as f_name_opened:
            # Displaying the opened file
            print("************************************* " +
                  "FILE \"{}\"".format(sys.argv[i],) +
                  " *************************************")
            print(f_name_opened.read().encode("latin-1").decode("utf-8"))
# Exception -> file not found
except FileNotFoundError:
    print("Warning, the file \"{}\" wasn't found.".format(sys.argv[i]))
    quit()
# All other exceptions
except:
    print("Warning, at least one file name must be provided as a command-line arguments.")
    quit()
