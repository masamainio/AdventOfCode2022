
import re
from pathlib import Path

filepath = Path()
filesizes = {}
    
with open("day7/day7_input.txt") as f:
    for line in f:
        line = line.strip("\n")

        if re.findall(r"^\$ cd /", line):
            filepath = Path(r"/")

        if re.findall(r"^\$ ls", line):
            continue
        
        if re.findall(r"\d+ \w+", line):
            size, name = re.split(" ", line)
            fp = filepath / name 
            for p in fp.parents:
                if p not in filesizes.keys():
                    filesizes[p] = int(size)
                else:
                    filesizes[p] += int(size)
        
        if re.findall(r"^dir", line):
            directory = re.split(" ", line)[1]
            fp = filepath / directory
        
        if re.findall(r"^\$ cd \w+", line):
            directory = re.split(" ", line)[2]
            filepath = filepath / directory
        
        if re.findall(r"^\$ cd \.\.", line):
            filepath = filepath.parent


print(f"Part 1 answer: {sum([v for v in filesizes.values() if v < 100_000])}")

space_required = 30_000_000 - (70_000_000 - max([v for v in filesizes.values()]))

print(f"Part 2 answer: {min([v for v in filesizes.values() if v > space_required])}")
