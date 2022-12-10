"""
Advent of Code 2022 - Day 2

"""

FILE_PATH = "day_2/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()

    # Get the shapes played by player 2 only
    player_2_shapes = [line.split()[1] for line in text_data]

    # Convert each player 2 shape to a score using a dict
    shape_score = {"X": 1, "Y": 2, "Z": 3}
    player_2_shape_score = sum([shape_score[shape] for shape in player_2_shapes])

    # Now get a list of player 1 & player 2 shapes combined
    combined_shapes = [line.replace(" ", "") for line in text_data]

    # Create a dictionary of all possible combinations and score outcomes
    win_score = {
        ("AX"): 3,
        ("AY"): 6,
        ("AZ"): 0,
        ("BX"): 0,
        ("BY"): 3,
        ("BZ"): 6,
        ("CX"): 6,
        ("CY"): 0,
        ("CZ"): 3
    }

    player_2_win_score = sum([win_score[shape_combo] for shape_combo in combined_shapes])

    print(player_2_shape_score + player_2_win_score)
