#%%


def read_data(filepath):
    _data = []
    with open(filepath) as f:
        for line in f:
            line = line.strip('\n')
            if line:
                _data.append([tuple(map(int, x.split("-"))) for x in line.split(",")])
    return _data


def part1(input):
    overlapping = 0
    for a in input:
        set1 = set(range(a[0][0], a[0][1] + 1))
        set2 = set(range(a[1][0], a[1][1] + 1))
        if not set1.isdisjoint(set2):
            if set1.issubset(set2) or set2.issubset(set1):
                overlapping += 1
    return overlapping


def part2(input):
    overlapping = 0
    for a in input:
        set1 = set(range(a[0][0], a[0][1] + 1))
        set2 = set(range(a[1][0], a[1][1] + 1))
        if not set1.isdisjoint(set2):
            overlapping += 1
    return overlapping


data = read_data(r"day4_input.txt")
print(f"Part 1 answer: {part1(data)}")
print(f"Part 2 answer: {part2(data)}")
# %%
