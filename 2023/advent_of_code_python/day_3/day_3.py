# def create_matrix(lines):
# 	matrix = []
# 	for line in lines:
# 		matrix_line = [char for char in line if char != '\n']
# 		matrix.append(matrix_line)
# 	return matrix
#
#
# def gear_ratio_matrix(filename):
# 	with open(filename, "r") as file:
# 		lines = file.readlines()
# 		return create_matrix(lines)
#
#
# def is_symbol(entry):
# 	return entry in "@*$&%+#-/="
#
#
# def get_number(line, start_position):
# 	position = start_position
# 	number = ''
# 	while position < len(line) and line[position].isnumeric():
# 		number += line[position]
# 		position += 1
# 	return number
#
#
# def iterate_matrix(matrix):
# 	digit_coordinates = {}
#
# 	for row_number, line in enumerate(matrix):
# 		current_row_symbols = set()
#
# 		column_position = 0
# 		while column_position < len(line):
# 			entry = line[column_position]
#
# 			if entry.isnumeric():
# 				full_number = get_number(line, column_position)
# 				start_pos = column_position
# 				end_pos = column_position + len(full_number) - 1
#
# 				# Check for adjacent symbol on the same line
# 				if any(pos in current_row_symbols for pos in [start_pos - 1]) or \
# 				   (end_pos + 1 < len(line) and line[end_pos + 1] in current_row_symbols):
# 					digit_coordinates.setdefault((row_number, start_pos), []).append(('line', full_number))
#
# 				# Check for adjacent symbol on the line above
# 				if row_number > 0:
# 					for pos in range(start_pos - 1, end_pos + 2):
# 						if pos >= 0 and pos < len(matrix[row_number - 1]) and is_symbol(matrix[row_number - 1][pos]):
# 							digit_coordinates.setdefault((row_number, start_pos), []).append(('above', full_number))
# 							break  # Break if any symbol is found
#
# 				column_position = end_pos
#
# 			elif is_symbol(entry):
# 				current_row_symbols.add(column_position)
#
# 			column_position += 1
#
# 	return digit_coordinates
#
#
# if __name__ == "__main__":
# 	actual_input = "input.txt"
# 	matrix = gear_ratio_matrix(actual_input)
# 	result = iterate_matrix(matrix)
# 	part_numbers = []
#
# 	for key, values in result.items():
# 		for value_tuple in values:
# 			condition, number = value_tuple
# 			print(f"Number '{number}' found at row {key[0] + 1}, column {key[1] + 1}, condition: {condition}")
# 			part_numbers.append(int(number))
#
# 	print(sum(part_numbers))
import re

def gear_ratio_matrix(filename):
	with open(filename, "r") as file:
		return [line.rsplit()[0] for line in file]

def verify_horizontal(string, start, end):
	if start == 0:
		string = string[start : end + 1]
	elif len(string) < end + 1:
		string = string[start - 1 : end]
	else:
		string = string[start - 1 : end + 1]

	pattern = re.compile("[^\w\.]")
	symbol = re.findall(pattern, string)
	if len(symbol) > 0:
		return True
	else:
		return False


def verify_diagonals(string, start, end):
	if start == 0:
		string = string[start: end + 1]
	elif len(string) < end + 1:
		string = string[start - 1: end]
	else:
		string = string[start - 1: end + 1]
	pattern = re.compile("[^\w\.]")
	symbols = re.findall(pattern, string)
	if len(symbols) > 0:
		return True
	else:
		return False


def create_empty_line(row, matrix):
	# added line above and below original matrix to simplify adjacent checks
	if row != 0:
		new_row_above = matrix[row - 1]
	else:
		new_row_above = "..." * 50
	if row != (len(matrix) - 1):
		new_row_below = matrix[row + 1]
	else:
		new_row_below = "..." * 50
	return new_row_below, new_row_above


def iterate_matrix(matrix):
	schematic_engine = []
	pattern = re.compile("\d+")
	for row, line in enumerate(matrix):
		digits = re.finditer(pattern, line)
		for number in digits:
			start = number.start()
			end = number.end()
			up, down = create_empty_line(row, matrix)
			if (
				verify_diagonals(up, start, end)
				or verify_diagonals(down, start, end)
				or verify_horizontal(line, start, end)
			):
				schematic_engine.append(int(number.group()))
	return schematic_engine


if __name__ == '__main__':
	example = gear_ratio_matrix("input.txt")
	schematic_engine = iterate_matrix(example)
	print(schematic_engine)
	print(len(schematic_engine))
	print(sum(schematic_engine))

# 535235
