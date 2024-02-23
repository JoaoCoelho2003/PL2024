# rules for the script: regular expressions only
# reads a file from the stdin: cat file.txt | python3 resolucaopy
# if the string "on" is found then any number after that will be incremented to a variable
# once the string "off" is found then the numbers after that are not taken into account
# if "on" appears once again then it counts again, 2 or more "ons" or "offs" back to back will work as one "on" or "off"
# if the char "=" is found in the text, the value of the variable is printed, as the program finishes
# both on and off can be found in any tpye of combination of upper and lower case letters
# they can also be found "inside other words" like lonely has "on" inside

import sys
import re

def number_incrementer(data):
    counter = 0.0
    on = False
    off = False
    for i in data.split():
        if re.search(r'on', i, re.IGNORECASE):
            on = True
            off = False
        if re.search(r'off', i, re.IGNORECASE):
            off = True
            on = False
        if re.search(r'\d+', i) and on and not off:
            counter += float(i)
        if re.search(r'=', i):
            return counter



def main():
    data = sys.stdin.read()
    print(number_incrementer(data))

if __name__ == "__main__":
    main()