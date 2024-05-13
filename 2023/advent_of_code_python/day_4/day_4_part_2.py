"""
Use memoisation to calculate the number of card copies.
The card numbers increase by a factor of one so can just use a list to hold the copies and use the indice as the card number.
Initialize a dictionary num_dict that stores the amount of each card with 1 for each card.
Then I iterated through each cardnumber (line) and added the value num_dict[cardnumber] to each value from cardnumber+1 to cardnumber+1+len(winningsnumbers).
Then I summed up the values of each key and it completed in less than 2 seconds.
"""

# def get_input(filename):
# 	with open(filename, "r") as file:
# 		return [line for line in file]
#
#
# def parse_input(input_lists):
# 	matched_nums = []
# 	for i in input_lists:
# 		lines = i.strip().split("\n")
# 		for i in lines:
# 			i = i.replace(",,", ",")
# 			# Get card number
# 			card_number, numbers = i.split(":")
# 			card = int(card_number.split()[1])
#
# 			# Get game numbers & expected/valid numbers
# 			game_numbers, valid_numbers = numbers.split("|")
#
# 			# Write to dictionary where numbers are the key for easy/quick look up later
# 			gn = set(map(int, game_numbers.split()))
# 			vn = set(map(int, valid_numbers.split()))
#
# 			matches = len(vn.intersection(gn))
# 			matched_nums.append(matches)
# 			# output[card] = {"game_numbers": gn, "valid_numbers": vn}
#
# 	return matched_nums
#
#
# def make_matched_copies(matched_nums):
# 	copied_matches = []
# 	for card_number, matches in enumerate(matched_nums):
# 		for copy in range(card_number+1, card_number+1+matches):
# 			print(copy)
# 			copied_matches.append(copy)
# 	return copied_matches
#
#
# if __name__ == '__main__':
# 	inputs = get_input("input.txt")
# 	matched_nums = parse_input(inputs)
# 	print(matched_nums)
# 	make_matched_copies(matched_nums)
# 	print(sum(total_cards.values()))


import re

with open('input.txt', 'r') as file:
	lines = file.readlines()

	pattern = re.compile(r'Card\s+(\d+):\s+([\d\s]+)\s*\|\s*([\d\s]+)')
	pile_points = 0
	cards_instances = [1] * len(lines)
	for entry in lines:
		match = pattern.search(entry)

		card_num = int(match.group(1))
		group1_numbers = list(map(int, match.group(2).split()))
		group2_numbers = list(map(int, match.group(3).split()))

		common_elements_count = len(set(group1_numbers) & set(group2_numbers))
		pile_points += 2 ** (common_elements_count - 1) if common_elements_count >= 1 else 0

		for idx in range(common_elements_count):
			cards_instances[card_num + idx] += cards_instances[card_num - 1]

	print(f"Part 1: {pile_points}")
	print(f"Part 2: {sum(cards_instances)}")

"""
Part 1: 23847
Part 2: 8570000
"""