# """
# Iterate through the matrix and search for "*"
# Then find if there are adjacent numbers to the asterisk. If there are two adjecent numbers, then
# ratios.append(number_1 * number_2)
# Then sum all of the ratios to output the final number
# sum(ratios)
# """
#
# import re
# import ast
#
#
# def create_matrix():
# 	with open("input.txt", "r") as file:
# 		return [line.rsplit()[0] for line in file]
#
#
# def create_empty_line(row, matrix):
# 	# added line above and below original matrix to simplify adjacent checks
# 	if row != 0:
# 		new_row_above = matrix[row - 1]
# 	else:
# 		new_row_above = "..." * 50
# 	if row != (len(matrix) - 1):
# 		new_row_below = matrix[row + 1]
# 	else:
# 		new_row_below = "..." * 50
# 	return new_row_below, new_row_above
#
#
# def verfiy_horizontal(string, start):
# 	left = string[:start]
# 	right = string[start + 1:]
#
# 	pattern_left = re.compile("(\d+)$")
# 	numbers_left = re.findall(pattern_left, left)
#
# 	pattern_right = re.compile("^(\d+)")
# 	numbers_right = re.findall(pattern_right, right)
#
# 	return numbers_left + numbers_right
#
#
# def verify_diagonal(string, start):
# 	pattern = re.compile("\d+")
# 	numbers = re.finditer(pattern, string)
#
# 	adjacent = []
# 	for number in numbers:
# 		number_range = range(number.start(), number.end())
# 		if (
# 				(start in number_range)
# 				or (start - 1 in number_range)
# 				or (start + 1 in number_range)
# 		):
# 			adjacent.append(number.group())
#
# 	return adjacent
#
#
# def iterate_matrix(matrix):
# 	ratios = []
# 	pattern = re.compile('\*')
# 	for row, line in enumerate(matrix):
# 		asterisks = re.finditer(pattern, line)
# 		for asterisk in asterisks:
# 			start = asterisk.start()
# 			up, down = create_empty_line(row, matrix)
# 			numbers_horizontal_alignment = verfiy_horizontal(line, start)
# 			numbers_above_alignment = verify_diagonal(up, start)
# 			numbers_under_alignment = verify_diagonal(down, start)
#
# 			numbers = [n for n in (numbers_horizontal_alignment, numbers_above_alignment, numbers_under_alignment) if n]
#
# 			# Check if there are exactly 2 lists in numbers, and then calculate the product of their first elements
# 			if len(numbers) == 2:
# 				ratios.append(int(numbers[0][0]) * int(numbers[1][0]))
#
# 	# print(int(numbers[1]))
# 	return ratios
#
#
# if __name__ == "__main__":
# 	matrix = create_matrix()
# 	ratios = iterate_matrix(matrix)
# 	print(sum(ratios))

"""
Iterate through the matrix and search for "*"
Then find if there are adjacent numbers to the asterisk. If there are two adjecent numbers, then
ratios.append(number_1 * number_2)
Then sum all of the ratios to output the final number
sum(ratios)
"""
import re

with open("input.txt") as f:
    content = [line.rsplit()[0] for line in f]


def verfiy_horizontal(string, start):
    left = string[:start]
    right = string[start + 1 :]

    pattern_left = re.compile("(\d+)$")
    numbers_left = re.findall(pattern_left, left)

    pattern_right = re.compile("^(\d+)")
    numbers_right = re.findall(pattern_right, right)

    return numbers_left + numbers_right


def verify_diagonal(string, start):
    pattern = re.compile("\d+")
    numbers = re.finditer(pattern, string)

    adjacent = []
    for number in numbers:
        number_range = range(number.start(), number.end())
        if (
            (start in number_range)
            or (start - 1 in number_range)
            or (start + 1 in number_range)
        ):
            adjacent.append(number.group())

    return adjacent


gear_ratios = []
example = content
for i, line in enumerate(example):
    pattern = re.compile("\*")
    check = re.finditer(pattern, line)
    for asteriks in check:
        start = asteriks.start()
        end = asteriks.end()

        if i != 0:
            up = example[i - 1]
        else:
            up = "..." * 50
        if i != (len(example) - 1):
            down = example[i + 1]
        else:
            down = "..." * 50

        numbers_h = verfiy_horizontal(line, start)
        numbers_u = verify_diagonal(up, start)
        numbers_d = verify_diagonal(down, start)

        numbers = numbers_h + numbers_u + numbers_d
        if len(numbers) == 2:
            gear_ratios.append(int(numbers[0]) * int(numbers[1]))


print(sum(gear_ratios))


# 79844424