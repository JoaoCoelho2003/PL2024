import sys
import re

def number_incrementer(data):
    sum = 0
    all_occurrences = re.findall(r'(on|off|=|\d+)', data, re.IGNORECASE)
    on = False
    print(all_occurrences)

    for occurrence in all_occurrences:
        if occurrence.lower() == "on":
            on = True
        elif occurrence.lower() == "off":
            on = False
        elif occurrence == "=":
            print(sum)
        elif on:
            sum += int(occurrence)

def main():
    data = sys.stdin.read()
    number_incrementer(data)

if __name__ == "__main__":
    main()
