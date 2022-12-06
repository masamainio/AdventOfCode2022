#%%
import re


def read_data(filepath):
    boxes = []
    instructions = []
    reg1 = re.compile("\[\w{1}\]|[\r ]{4}")
    reg2 = re.compile("move \d+ from \d to \d")

    with open(filepath) as f:
        for line in f:
            line = line.strip("\n")
            if line:
                if re.findall(reg1, line):
                    res = re.findall(reg1, line)
                    lst = [x[:3] for x in res if len(x) > 2]
                    boxes.append(lst)
                elif re.findall(reg2, line):
                    res = re.findall(r"\d+", line)
                    instructions.append([int(x) for x in res])
    boxes1 = [list(x)[::-1] for x in zip(*boxes)]
    for i in range(len(boxes1)):
        boxes1[i] = [x for x in boxes1[i] if x != "   "]
    return boxes1, instructions


def part1(box, instructions):

    inst1 = instructions.pop(0)

    boxes_count = -1 * (inst1[0] + 1)
    src_col = inst1[1] - 1
    trg_col = inst1[2] - 1

    box[trg_col] += box[src_col][-1:boxes_count:-1]
    del box[src_col][-1:boxes_count:-1]

    if len(instructions) == 0:
        return
    elif len(instructions) >= 1:
        return part1(box, instructions)


def part2(box, instructions):

    inst1 = instructions.pop(0)

    boxes_count = inst1[0]
    src_col = inst1[1] - 1
    trg_col = inst1[2] - 1

    box[trg_col] += box[src_col][-boxes_count:]
    del box[src_col][-boxes_count:]

    if len(instructions) == 0:
        return
    elif len(instructions) >= 1:
        return part2(box, instructions)


box, inst = read_data(r"day5_input.txt")
part1(box, inst)
answer = "".join([str(x[-1]).strip("[").strip("]") if x else " " for x in box])
print(f"Part 1 answer: {answer}")

box, inst = read_data(r"day5_input.txt")
part2(box, inst)
answer = "".join([str(x[-1]).strip("[").strip("]") if x else " " for x in box])
print(f"Part 2 answer: {answer}")


# %%
