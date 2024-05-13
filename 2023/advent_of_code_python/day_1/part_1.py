"""
Open txt file
Parse txt data.
Iterate through each line.
Use regex to find integers. or isattr()/is type()?
If one integer found, multiply by itself.
If multiple integers found, then only take 1st and last. Discard the rest.
must use the first digit and the last digit to form a two-digit number
Add each product of two multiples to an iterator and sum these. Output the total
"""
import re


def parse_file() -> list:
	with open("input.txt", 'r') as f:
		output: list = []
		for line in f:
			integers = re.findall(r'\d+', line)
			if integers:
				first_digit = integers[0][0]
				last_digit = integers[-1][-1]
				two_digit_number = int(first_digit + last_digit)
				output.append(two_digit_number)
			else:
				output.append(0)
		return output


if __name__ == "__main__":
	nums = parse_file()
	print(sum(nums))


# 54573
