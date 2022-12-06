#%%


def day6(filepath, unique_chars):
    with open(filepath) as f:
        for line in f:
            for i, char in enumerate(list(line)):
                if len(set(list(line[i:i+unique_chars]))) == unique_chars:
                    return i + unique_chars


print(f"Part 1 answer: {day6(r'day6_input.txt', 4)}")
print(f"Part 2 answer: {day6(r'day6_input.txt', 14)}")


# %%
