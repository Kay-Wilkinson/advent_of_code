
def get_input(filename):
	with open(filename, "r") as file:
		return [line for line in file]


def parse_input(input_lists):
	output = {}
	matched_nums = {}
	for i in input_lists:
		lines = i.strip().split("\n")
		for i in lines:
			i = i.replace(",,", ",")
			# Get card number
			card_number, numbers = i.split(":")
			card = int(card_number.split()[1])

			# Get game numbers & expected/valid numbers
			game_numbers, valid_numbers = numbers.split("|")

			# Write to dictionary where numbers are the key for easy/quick look up later
			gn = set(map(int, game_numbers.split()))
			vn = set(map(int, valid_numbers.split()))

			matches = [match for match in vn.intersection(gn)]
			matched_nums[card] = matches
			output[card] = {"game_numbers": gn, "valid_numbers": vn}

	return output, matched_nums


def get_game_points(matches):
	power_ofs = []
	for k, v in matches.items():
		num_doubles = len(v)
		powers = 2 ** (num_doubles - 1)
		power_ofs.append(powers)
	return power_ofs


if __name__ == '__main__':
	inlists = get_input("input.txt")
	p, matched = parse_input(inlists)

	filtered_dict = {k: v for k, v in matched.items() if len(v) >= 1}

	powers = get_game_points(filtered_dict)
	print(sum(powers))

# 23847
