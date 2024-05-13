"""
Game parameters: 12 red cubes, 13 green cubes, and 14 blue cubes
Steps:
Open input file and read lines.
Write ID and values into dicts
Filter out any values that are above the parameters e.g. if red cubes exceed 12. if threshold reached, delete dict key
Iterate over all keys and extract digits into list
Sum list and return value as final product
"""
import re


def is_valid_sequence(sequence, valid_values) -> bool:
	for colour, max_value in valid_values.items():
		found_values = re.findall(fr"\d+\s(?={colour})", sequence)
		if any(int(value) > max_value for value in found_values):
			return False
	return True


def parse_data():
	game_dict = {}
	valid_values = {"red": 12, "green": 13, "blue": 14}
	with open("input.txt", "r") as f:
		for line in f:
			game_id, game_data = line.split(":", 1)
			sequences = [seq.strip().split(", ") for seq in game_data.split(";") if seq.strip()]
			game_dict[game_id.strip()] = sequences

	invalid_games = [game for game, sequences in game_dict.items() if not all(is_valid_sequence(' '.join(seq), valid_values) for seq in sequences)]
	for game in invalid_games:
		del game_dict[game]

	return game_dict


if __name__ == "__main__":
	output = []
	count = 0
	games = parse_data()
	digits = [int(re.findall(r'\d+', text)[0]) for text in games.keys() if re.findall(r'\d+', text)]

	print(sum(digits))

# 2563