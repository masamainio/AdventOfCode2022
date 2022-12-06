#%%

# Part 1
shape_points = {"Rock": 1,
                "Paper": 2,
                "Scissors": 3}

outcome_points = {"win": 6,
                  "draw": 3,
                  "lost": 0}

opponent = {"A": "Rock",
            "B": "Paper",
            "C": "Scissors"}

me = {"Y": "Paper",
      "X": "Rock",
      "Z": "Scissors"}


with open("day2_input.txt") as f:
    total_points = 0
    for line in f:
        line = line.strip('\n')
        if line:
            line_split = line.split(" ")
            op_choice = opponent.get(line_split[0])
            my_choice = me.get(line_split[1])
            total_points += + shape_points.get(my_choice)

            if op_choice == my_choice:
                total_points += outcome_points.get("draw")

            if op_choice == "Paper" and my_choice == "Scissors":
                total_points += outcome_points.get("win")

            if op_choice == "Rock" and my_choice == "Paper":
                total_points += outcome_points.get("win")

            if op_choice == "Scissors" and my_choice == "Rock":
                total_points += outcome_points.get("win")

print(f"Part 1 answer: {total_points}")


# %%

# Part 2
shape_points = {"Rock": 1,
                "Paper": 2,
                "Scissors": 3}

outcome_points = {"win": 6,
                  "draw": 3,
                  "lost": 0}

opponent = {"A": "Rock",
            "B": "Paper",
            "C": "Scissors"}

me = {"Y": "draw",
      "X": "lost",
      "Z": "win"}


with open("day2_input.txt") as f:
    total_points = 0
    for line in f:
        line = line.strip('\n')
        if line:
            line_split = line.split(" ")
            op_choice = opponent.get(line_split[0])
            my_choice = me.get(line_split[1])

            if my_choice == "win":
                if op_choice == "Rock":
                    my_shape = "Paper"
                if op_choice == "Paper":
                    my_shape = "Scissors"
                if op_choice == "Scissors":
                    my_shape = "Rock"
                total_points += outcome_points.get("win")

            if my_choice == "draw":
                my_shape = op_choice
                total_points += outcome_points.get("draw")

            if my_choice == "lost":
                if op_choice == "Rock":
                    my_shape = "Scissors"
                if op_choice == "Paper":
                    my_shape = "Rock"
                if op_choice == "Scissors":
                    my_shape = "Paper"

            total_points += + shape_points.get(my_shape)

print(f"Part 2 answer: {total_points}")


# %%
