"""
Iterate through file. Assume that line length is equal for each line.
Create matrix grid from file lines. Assume that grid 
Iterate through matrix until a number is found. Find the start and finish positions of the number. Log the row_number, start_position and finish_position.
Go through row_number +1 and row_number -1 to the start_position -1 and finish_position +1 (for diagonals) of that number. Find if a symbol, log the original number

(Disregard full stops)
Sum all logged numbers
"""

import re


def create_matrix(lines):
	matrix = []
	for line in lines:
		matrix_line = [char for char in line if char != '\n']
		matrix.append(matrix_line)
	return matrix


def gear_ratio_matrix(filename):
	with open(filename, "r") as file:
		lines = file.readlines()
		return create_matrix(lines)


def is_symbol(entry):
	return entry != '.' and not entry.isnumeric()


def get_number(line, start_position):
	position = start_position
	number = ''
	while position < len(line) and line[position].isnumeric():
		number += line[position]
		position += 1
	return number


def scan_above_line(previous_line, column_position, found_symbol_coordinates, max_row_length):
	left_diagonal, right_diagonal = get_diagonals(column_position, max_row_length)
	# Find above symbols
	if previous_line in found_symbol_coordinates.keys():
		# Find symbol directly above
		if column_position in found_symbol_coordinates.get(previous_line):
			return True
		# Find if diagonal
		elif left_diagonal in found_symbol_coordinates.get(previous_line):
			return True
		elif right_diagonal in found_symbol_coordinates.get(previous_line):
			return True
		else:
			return False
	else:
		return False


def get_diagonals(column_position, max_row_len):
	# This current implementation will mean that the outer edges of the matrix get checked twice so may refactor later
	if column_position >= 1:
		left_diagonal = column_position - 1
		if column_position < max_row_len:
			right_diagonal = column_position + 1
		else:
			right_diagonal = column_position
	else:
		left_diagonal = column_position
	return left_diagonal, right_diagonal


def is_part_number(entry, row_number, column_position, line, max_row_length):
	found_symbol_coordinates = {}
	previous_line = row_number - 1

	left = column_position - 1
	right = column_position + 1

	# Handle symbols
	if not entry.isnumeric():
		found_symbol_coordinates.update({row_number: column_position})
	# Handle digits
	else:
		# Find if entry has adjacent symbol
		if is_symbol(line[left]):
			return entry
		if is_symbol(line[right]):
			return entry
		# Find if symbols on row above unless this is the starting line
		elif row_number != 0:
			if scan_above_line(previous_line, column_position, found_symbol_coordinates, max_row_length):
				return entry
		else:
			return None


def get_digit_end_index(entry, start_position, line, max_length, row_number):
	end_position = int(line[start_position])
	while end_position < max_length and line[end_position].isnumeric():
		end_position += 1
	return end_position - 1


def iterate_matrix(matrix):
	digit_coordinates = {}
	previous_symbols = set()
	for row_number, line in enumerate(matrix):
		current_symbols = set()
		column_position = 0
		while column_position < len(line):
			entry = line[column_position]
			if is_symbol(entry):
				current_symbols.add(column_position)
			elif entry.isnumeric():
				full_number = get_number(line, column_position)
				end_position = column_position + len(full_number) - 1
				if any(adjacent in current_symbols for adjacent in [column_position - 1, end_position + 1]):
					digit_coordinates[(row_number, column_position)] = full_number
				elif row_number > 0 and any(adjacent in previous_symbols for adjacent in get_diagonals(column_position, len(line)) + get_diagonals(end_position, len(line))):
					digit_coordinates[(row_number, column_position)] = full_number
				column_position = end_position
			column_position += 1
		previous_symbols = current_symbols
	return digit_coordinates


if __name__ == "__main__":
	test_input = "test_input.txt"
	actual_input = "input.txt"
	matrix = gear_ratio_matrix(test_input)
	matrix_row_len = len(matrix)
	matrix_col_len = len(matrix[0])
	digit_coordinates = iterate_matrix(matrix)
	print(digit_coordinates)
