"""
Classify each hand and bid
determine type of hand
Link type of hand to strength. Assign strength values 
Sort hands
Calculate total winnings
"""


def extract_data(input_data):
	with open(input_data, 'r') as file:
		return [line.strip().split() for line in file]


def get_card_value(card):
	card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
				   '2': 2}
	return card_values[card]


def classify_hand(hand):
	# Count occurrences of each card
	card_count = {}
	for card in hand:
		card_value = get_card_value(card)
		card_count[card_value] = card_count.get(card_value, 0) + 1

	# Sort by count and then by value if counts are equal
	sorted_counts = sorted(card_count.items(), key=lambda x: (-x[1], -x[0]))

	# Flatten the sorted counts into a single list to determine strength
	strength = []
	for value, count in sorted_counts:
		strength.extend([value] * count)

	# Determine the hand type
	counts = [count for _, count in sorted_counts]
	if counts == [5]:
		hand_type = 7  # Five of a kind
	elif counts == [4, 1]:
		hand_type = 6  # Four of a kind
	elif counts == [3, 2]:
		hand_type = 5  # Full house
	elif counts == [3, 1, 1]:
		hand_type = 4  # Three of a kind
	elif counts == [2, 2, 1]:
		hand_type = 3  # Two pair
	elif counts == [2, 1, 1, 1]:
		hand_type = 2  # One pair
	else:
		hand_type = 1  # High card

	# Return hand type and strength as a tuple
	return hand_type, tuple(strength)


def calculate_winnings(hands):
	ranked_hands = []
	for hand, bid in hands:
		hand_type, strength = classify_hand(hand)
		ranked_hands.append((hand_type, strength, int(bid)))

	ranked_hands.sort(key=lambda x: (x[0], x[1]), reverse=True)
	total_winnings = sum(bid * (rank + 1) for rank, (_, _, bid) in enumerate(ranked_hands))
	return total_winnings


input_data = 'input.txt'
test_input = 'test_input.txt'

cards = extract_data(input_data)


# print(calculate_winnings(cards))
def parseInput(path):
	result = []

	def convertToNum(n):
		if n.isnumeric():
			return int(n)
		else:
			return n

	file = open(path, 'r')
	for line in file.readlines():
		line = (line.replace('\n', '').split(' '))
		line = list(map(lambda x: convertToNum(x), line))
		result.append(line)
	result = list(map(lambda x: {'hand': x[0], 'bet': x[1]}, result))
	return (result)


def makeCountObj(hand):
	arr = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	results = {}
	for card in arr:
		results[card] = 0
	for card in str(hand):
		results[card] = results[card] + 1
	for card in arr:
		if results[card] == 0:
			del results[card]
	return results

input = parseInput(input_data)
for cards in input:
	countOfCards = makeCountObj(cards['hand'])
	print(countOfCards)
