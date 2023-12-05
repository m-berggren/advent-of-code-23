import sys

sum_of_calibrations = 0

with open(sys.argv[1], 'r') as file:

    for line in file:
        find_first = True
        first_char = ""
        last_char = ""

        for char in line:
            if char.isdigit():
                if find_first:
                    first_char = char
                    last_char = char
                    find_first = False
                else:
                    last_char = char
        concat_chars = first_char + last_char
        sum_of_calibrations += int(concat_chars)

print(sum_of_calibrations)