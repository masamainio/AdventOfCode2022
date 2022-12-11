
with open("day8/day8_input.txt") as f:
    treegrid1 = [[int(n) for n in line.strip("\n")] for line in f]

cols = len(treegrid1)
rows = len(treegrid1[0])

treegrid2 = [[x[i] for x in treegrid1] for i in range(rows)]

# Part 1
result1 = [[True for x in range(rows)] for x in range(cols)]

for i_row in range(0, rows):
    for i_col in range(0, cols):
        tree = treegrid1[i_row][i_col]
        if not (
            all(tree > x for x in treegrid1[i_row][i_col+1:])
            or all(tree > x for x in treegrid1[i_row][:i_col][::-1])
            or all(tree > x for x in treegrid2[i_col][i_row+1:])
            or all(tree > x for x in treegrid2[i_col][:i_row][::-1])
        ):
            result1[i_row][i_col] = False

result1[0] = [True for x in range(rows)]
result1[-1] = [True for x in range(rows)]

print(f"Part 1 answer: {sum([sum(x) for x in result1])}")

# Part 2
result2 = [[0 for x in range(rows)] for x in range(cols)]

def get_sum(value, line):
    _sum = 0
    for n in line:
        _sum += 1
        if n >= value:
            break
    return _sum


for i_row in range(0, rows):
    for i_col in range(0, cols):
        tree = treegrid1[i_row][i_col]
        sum_r = get_sum(tree, treegrid1[i_row][i_col + 1 :])
        sum_l = get_sum(tree, treegrid1[i_row][:i_col][::-1])
        sum_u = get_sum(tree, treegrid2[i_col][i_row + 1 :])
        sum_d = get_sum(tree, treegrid2[i_col][:i_row][::-1])
        result2[i_row][i_col] = sum_r * sum_l * sum_u * sum_d

print(f"Part 2 answer: {max([max(x) for x in result2])}")
