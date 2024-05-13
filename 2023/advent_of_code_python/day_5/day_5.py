"""
part 1: you are given 4 seeds, and a bunch of maps each with its own lines, like this: (a, b, c)

a, b, c means: [b, b + c) is transformed to [a, a + c) (square bracket inclusive, round bracket exclusive).

with the given example, [98, 100) is transformed to [50, 52), in other words, 98 => 50, 99 => 51, (note 100 is not included here).

Similarly, [50, 98) => [52, 100) means 50 => 52, 51 => 53.....97 => 99.

So the given seed 79 is turned into soil 81.

Next map:

[15, 52) => [0, 37); then [52, 54) => [37, 39); [0, 15) => [39, 54)

Since 81 is not in any of these ranges, soil 81 is turned into fertilizer 81.

Similarly, fertilizer 81 = water 81 (no transformation range for fertilizer to water includes 81).

Last example: water to light.

[18, 25) => [88, 95); [25, 95) => [18, 88). So 81 is in the second transformation, and is turned into light 74.

What you need to do: turn the 4 given seeds into soil, then from soil to fertilizer, then from fertilizer to water .... lastly from humidity to location. The minimum of the 4 result locations is the answer.
"""


def parse_data(path):
	data = []
	with open(path, 'r') as file:
		for index, line in enumerate(file):
			if index == 0:
				seeds = line.replace('seeds: ', '').replace('\n', '').split(' ')
				seeds = list(map(lambda x: int(x), seeds))
			if index > 0:
				data.append(line.replace('\n', ''))
		filtered_list = list(filter(lambda x: x != '', data))
		return filtered_list, seeds


def splitArray(arr):
	arrLen = len(arr)
	splitIndexes = [index for index, line in enumerate(arr) if line.__contains__('map')]
	splitIndexes.append(arrLen)
	splitArray = [arr[a:b] for a, b in zip([0] + splitIndexes, splitIndexes)]
	splitArrayLen = len(splitArray)
	splitArray = splitArray[1:splitArrayLen]
	return splitArray


def parse_input_data(path):
	data_dict = {}
	current_key = None
	with open(path, 'r') as file:
		for index, line in enumerate(file):
			if index == 0:
				seeds = line.strip().replace('seeds: ', '').split(' ')
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

	return data_dict, seeds


def find_location_in_almanac(data_dict, seeds):
	def get_target_value_range(target_value, source_start, destination_start):
		difference = target_value - source_start
		print(f'{target_value} is greater than {source_start} by {difference}')
		print(f'new target value is {destination_start} + {difference} = {destination_start + difference}')
		return destination_start + difference

	def find_location(seed_number):
		target_value = seed_number
		target_source = 'seed'
		for k, v in data_dict:
			print(k)
			print(v)

	seed_results = []
	for seed_number in data_dict:
		seed_results.append(find_location(seed_number))
	# print(min(seed_results))




def makeListObj(arr):
	listObj = []
	for line in arr:
		lineResult = []
		name = line[0].replace(' map:', '').split('-to-')
		sourceDestMap = line[1::]
		sourceDestMap = list(map(lambda x: x.split(' '), sourceDestMap))
		sequences = []
		for sequence in sourceDestMap:
			sequence = list(map(lambda x: int(x), sequence))
			sequences.append(sequence)
		sourceDestMap = sequences
		lineResult = {
			'name': name,
			'keys': sequences
		}
		listObj.append(lineResult)
	return (listObj)


def findLocations(listObj, seedNumbers):
	def changeTargetValue(targetValue, sourceStart, destStart):
		difference = targetValue - sourceStart
		# print(f'{targetValue} is greater than {sourceStart} by {difference}')
		# print(f'new target value is {destStart} + {difference} = {destStart + difference}')
		return destStart + difference

	def findLocation(seedNum):
		# print(f'searching seed {seedNum}')
		targetValue = seedNum
		targetSource = 'seed'
		for obj in listObj:
			source = obj['name'][0]
			# print("Source: ", source, "Target: ", targetSource)
			destination = obj['name'][1]
			if source == targetSource:
				print(f'reviewing {destination}: {obj["keys"]}')
				valSet = False
				for arr in obj['keys']:
					destStart = arr[0]
					sourceStart = arr[1]
					sourceRangeEnd = arr[2]
					isFound = targetValue >= sourceStart and targetValue <= sourceStart + sourceRangeEnd - 1

					if isFound and valSet == False:
						print(f'targetNumber {targetValue} is between {sourceStart} and {sourceStart + sourceRangeEnd - 1}')
						targetValue = changeTargetValue(targetValue, sourceStart, destStart)
						valSet = True
					# else:
					print(f'targetNumber {targetValue} is not between {sourceStart} and {sourceStart + sourceRangeEnd - 1}')
					targetSource = destination
				valSet = False
			print(destination, targetValue)
		return (targetValue)

	seedResults = []
	for seedNum in seedNumbers:
		seedResults.append(findLocation(seedNum))
	print(min(seedResults))


input_path = 'input.txt'
test_path = 'test_input.txt'
data_dict, seeds = parse_data(input_path)
print(data_dict)
# find_location_in_almanac(data_dict, seeds)

splitArray = splitArray(data_dict)
listObj = makeListObj(splitArray)
findLocations(listObj, seeds)
# print("Printing listObj")
# print(listObj)
# print(flist)
# print(seeds)


# Part 1: 389056265
