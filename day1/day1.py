# Part 1

with open("day1/day1_input.txt") as f:
    highest = 0
    total = 0
    for line in f:
        line = line.strip('\n')
        if line:
            total += int(line)
        else:
            if total > highest:
                highest = total
            total = 0

print(f"Part 1 answer: {highest}")

# Part 2
with open("day1/day1_input.txt") as f:
    highest = []
    total = 0
    for line in f:
        line = line.strip('\n')
        if line:
            total += int(line)
        else:
            highest.append(total)
            total = 0

print(f"Part 2 answer: {sum(sorted(highest, reverse=True)[:3])}")
