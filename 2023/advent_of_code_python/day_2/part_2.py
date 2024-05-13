"""
Return fewest number of cubes of each colour to make the game possible

Iterate through the nested list for each game and find the highest value per colour per game.
This should produce 3 integers (20 red, 15 blue, 3 green)
Multiply each integer together e.g. 20 * 15 * 3 to produce the power of that game
Return the sum of those powers

"""
import re


def is_valid_sequence(sequence, valid_values) -> bool:
	for colour, max_value in valid_values.items():
		found_values = re.findall(fr"\d+\s(?={colour})", sequence)
		if any(int(value) > max_value for value in found_values):
			return False
	return True


def find_highest_values(data_dict):
    results = {}

    for game, sequences in data_dict.items():
        highest_values = {'red': [0, ''], 'blue': [0, ''], 'green': [0, '']}

        for sequence in sequences:
            for item in sequence:
                # Ensure that item is a string
                if isinstance(item, str):
                    color = item.split()[-1]
                    value = int(re.findall(r'\d+', item)[0])
                    if value > highest_values[color][0]:
                        highest_values[color] = [value, item]
                else:
                    print(f"Unexpected data format for item in {game}: {item}")

        highest_digits = [highest_values[color][0] for color in highest_values]
        results[game] = highest_digits

    return results

def build_dict(valid_values):
	game_dict = {}
	with open("input.txt", "r") as f:
		for line in f:
			game_id, game_data = line.split(":", 1)
			sequences = [seq.strip().split(", ") for seq in game_data.split(";") if seq.strip()]
			game_dict[game_id.strip()] = sequences

	# invalid_games = [game for game, sequences in game_dict.items() if not all(is_valid_sequence(' '.join(seq), valid_values) for seq in sequences)]
	# for game in invalid_games:
	# 	del game_dict[game]

	return game_dict


if __name__ == "__main__":
	valid_values = {"red": 12, "green": 13, "blue": 14}
	filtered_values = build_dict(valid_values)
	"""
	Iterate through each key-value pair in the dictionary.
	For each value (which is a list of lists), iterate through the nested lists.
	In each nested list, compare the strings to find the one with the highest number.
	Extract and return only the digits from these highest value strings.
	"""

	powers = find_highest_values(filtered_values)
	print(powers)

	"""
	Create the powers of and sum
	"""
	p = [power[0] * power[1] * power[2] for power in powers.values()]

	print(sum(p))

# 70768



