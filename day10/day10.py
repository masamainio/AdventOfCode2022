# Data
numbers = []
cycles = []
cumsums = []

with open(r"day10/day10_input.txt") as f:
    cumsum = 1
    current_number = 1
    for line in f:
        line = line.strip("\n").split(" ")
        cumsums.append(cumsum)

        if line[0] == "noop":
            numbers.append(cumsum)
            cycles.append(1)
            continue

        elif line[0] == "addx":
            numbers.append(cumsum)
            numbers.append(cumsum)
            cycles.append(2)
            current_number = int(line[1])
            cumsum += current_number

# Part 1
total = 0
for pos in [20, 60, 100, 140, 180, 220]:
    total += numbers[pos-1] * pos

print(f"Part 1 answer: {total}")


# Part 2
result = []
result_str = ""
index = 0

for num, cycle in zip(cumsums, cycles):
    sprite = list(range(num-1, num+2))
    for i in range(cycle):
        if index in sprite:
            result_str += "#"
        else:
            result_str += "."
        index += 1
        if index % 40 == 0:
            result.append(result_str)
            result_str = ""
            index = 0

print("Part 2 answer:")
for row_st in result:
    print(row_st)
