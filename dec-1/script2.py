import sys

transpose = [
    ['one', 'one1one'],
    ['two', 'two2two'],
    ['three', 'three3three'],
    ['four', 'four4four'],
    ['five', 'five5five'],
    ['six', 'six6six'],
    ['seven', 'seven7seven'],
    ['eight', 'eight8eight'],
    ['nine', 'nine9nine'],
]

sum_of_calibrations = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        first_found = True
        first_char = ""
        last_char = ""

        for num, string in enumerate(transpose):
            line = line.replace(transpose[num][0], transpose[num][1])

        for char in line:
            if char.isdigit():
                if first_found:
                    first_char = char
                    last_char = char
                    first_found = False
                else:
                    last_char = char

        sum_of_calibrations += int(first_char + last_char)

print(sum_of_calibrations)
