from collections import OrderedDict


def parse_input_data(path):
	data_dict = {}
	current_key = None
	with open(path, 'r') as file:
		for index, line in enumerate(file):
			if index == 0:
				seeds = line.strip().replace('seeds: ', '').replace('\n', '').split(' ')
				seeds = list(map(int, seeds))
			else:
				line = line.strip()
				if line.endswith(':'):
					current_key = line
					keys = current_key.replace(' map:', '').split('-to-')
					key = (keys[0], keys[1])
					data_dict[key] = []
				elif current_key:
					data_dict[key].append(line)

	return OrderedDict(reversed(list(data_dict.items()))), seeds


def seed_map(seeds):
	split_indexes = [index for index, item in enumerate(seeds) if not index % 2]
	split_indexes.append(len(seeds))
	seed_map = [seeds[a:b] for a, b in zip([0] + split_indexes, split_indexes)][1::]
	return (seed_map)


def get_seed_from_location(data_dict):
	def change_target_value(target_value, source_start, destination_start):
		difference = target_value - destination_start
		return source_start + difference

	def check_for_valid_seed(target_value):
		is_valid = False
		for i in new_seeds:
			is_match = target_value >= i[0] and target_value <= i[0] + i[1] - 1
			if is_match:
				is_valid = True
				return is_valid
		return is_valid

	def find_seed(location_number):
		target_value = location_number
		target_destination = 'location'
		for k, v in data_dict:
			source = k[0]
			destination = k[1]
			if target_destination == destination:
				value_set = False
				for element in v:
					destination_start = v[0]
					source_start = v[1]
					destination_range_end = v[2]
					is_found = target_value >= destination_start and target_value <= destination_start + destination_range_end -1
					if is_found and value_set != True:
						target_value = change_target_value(target_value, source_start, destination_start)
						value_set = True
					target_destination = source
				value_set = False
			print(f'is {target_value} a valid seed number (evaluation location #{location_number}?')
			if check_for_valid_seed(target_value):
				print(f'{location_number} is a valid location')
				return True
			else:
				return False
	i = 0
	while find_seed(i) == False:
		i = i + 1


input_path = 'input.txt'
test_path = 'test_input.txt'
data_dict, seeds = parse_input_data(input_path)
# print(data_dict)
new_seeds = seed_map(seeds)
get_seed_from_location(data_dict)
# print(new_seeds)
# print(data_dict)


