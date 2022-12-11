# Part 1
import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

compartment1 = []
compartment2 = []

with open("day3/day3_input.txt") as f:
    total_points = 0
    for line in f:
        line = line.strip('\n')
        if line:
            splitter = len(line)//2
            compartment1.append(line[:splitter])
            compartment2.append(line[splitter:])


sum_of_prior = 0

for comp1, comp2 in zip(compartment1, compartment2):
    FOUND = False
    for letter in comp1:
        if not FOUND:
            if letter in comp2:
                sum_of_prior += alphabet.index(letter) + 1
                FOUND = True

print(f"Part 1 answer: {sum_of_prior}")


# Part 2

rucksacks = []
with open("day3/day3_input.txt") as f:
    total_points = 0
    for line in f:
        line = line.strip('\n')
        if line:
            rucksacks.append(line)

groups = [rucksacks[x:x+3] for x in range(0, len(rucksacks), 3)]

sum_of_prior = 0

for group in groups:
    FOUND = False
    for letter in group[0]:
        if not FOUND:
            if letter in group[1] and letter in group[2]:
                sum_of_prior += alphabet.index(letter) + 1
                FOUND = True

print(f"Part 2 answer: {sum_of_prior}")
