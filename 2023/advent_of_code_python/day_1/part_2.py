# from word2number import w2n


# print(sum([int(str(sublist[0]) + str(sublist[-1])) for sublist in [[__import__('word2number.w2n').w2n.word_to_num(item) if item.isalpha() else int(item) for sublist in [__import__('re').findall(r'\d|' + '|'.join(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']), item) for item in __import__('re').split('(\\D+|\\d)', line.replace('eighthree', 'eightthree').replace('eightwo', 'eighttwo').replace('oneight', 'oneeight').replace('twone', 'twoone').replace('threeight', 'threeeight').replace('fiveight', 'fiveeight').replace('sevenine', 'sevennine'))] for item in sublist] for line in open('input.txt', 'r').readlines()]]))
import re
from word2number import w2n


def convert_to_number(word):
	if word.isalpha():
		return w2n.word_to_num(word)
	else:
		return int(word)


def replace_edge_case_string_patterns(line):
	line = line.replace('eighthree', 'eightthree').replace('eightwo', 'eighttwo').replace(
		'oneight', 'oneeight').replace('twone', 'twoone').replace('threeight', 'threeeight').replace(
		'fiveight', 'fiveeight').replace('sevenine', 'sevennine')
	return line


def process_line(line):
	# Handle special cases in the string
	line = replace_edge_case_string_patterns(line)
	# Define the pattern
	pattern = r'\d|' + '|'.join(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])

	# Split the line and find all matches
	items = re.split(r'(\D+|\d)', line)
	numbers = [convert_to_number(item) for sublist in items for item in re.findall(pattern, sublist)]

	# Return the sum of the first and last number in the list
	return sum([int(str(numbers[0]) + str(numbers[-1]))])


# Read the file and process each line
with open('input.txt', 'r') as file:
	total = sum(process_line(line) for line in file)

print(total)

# 54591
