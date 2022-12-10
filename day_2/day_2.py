"""
Advent of Code 2022 - Day 2

"""

FILE_PATH = "day_2/input.txt"

with open(FILE_PATH, "r", encoding="utf-8") as input_file:

    text_data = input_file.read()
    text_data = text_data.splitlines()
    rounds = [line.replace(" ", "") for line in text_data]

    # Part 1
    # Create a dictionary of all possible combinations and score outcomes
    round_score = {
        ("AX"): 4, # draw + rock = 3 + 1
        ("AY"): 8, # win + paper = 6 + 2
        ("AZ"): 3, # lose + scissors = 0 + 3
        ("BX"): 1, # lose + rock = 0 + 1
        ("BY"): 5, # draw + paper = 3 + 2
        ("BZ"): 9, # win + scissors = 6 + 3
        ("CX"): 7, # win + rock = 6 + 1
        ("CY"): 2, # lose + paper = 0 + 2
        ("CZ"): 6 # draw + scissors = 3 + 3
    }

    player_2_score = sum([round_score[round] for round in rounds])
    print(player_2_score)

    # Part 2
    # Create dictionary for new decoding
    round_score_2 = {
        ("AX"): 3, # play scissors 3 + 0
        ("AY"): 4, # play rock 1 + 3
        ("AZ"): 8, # play paper 2 + 6
        ("BX"): 1, # play rock 1 + 0
        ("BY"): 5, # play paper 2 + 3
        ("BZ"): 9, # play scissors 3 + 6
        ("CX"): 2, # play paper 2 + 0
        ("CY"): 6, # play scissors 3 + 3
        ("CZ"): 7 # play rock 1 + 6
    }

    player_2_score_2 = sum([round_score_2[round] for round in rounds])
    print(player_2_score_2)
