"""
Starting speed: 0 meters per milisecond
1 mm = 1 mm/ps

distance travelled = remaining travel time * duration of button hold time
e.g. 12mm = 3ms * 4ms

Algorithm for Each Race:

For each race, we have a total race time T and a record distance D.

For each possible button hold time t (where t ranges from 0 to T), 
calculate the speed of the boat (speed = t) and the remaining time (remaining_time = T - t).

Calculate the distance the boat would travel (distance = speed * remaining_time).
Count the number of times the calculated distance is greater than the record distance D.
"""


def extract_data(input_data):
	with open(input_data, 'r') as file:
		race_stats = [line.strip().split() for line in file]
		times = [int(x) for x in race_stats[0][1:]]
		distances = [int(x) for x in race_stats[1][1:]]
		paired_data = list(zip(times, distances))
		return paired_data


def calculate_num_winning_options(races):
	total_ways = 1
	for race in races:
		print(f'Race data: {race}')
		time, record = race
		ways_to_win = 0
		for hold_time in range(time + 1):
			speed = hold_time
			remaining_time = time - hold_time
			print(f"Speed: {speed}. Remaining_time: {remaining_time}")
			distance = speed * remaining_time
			if distance > record:
				ways_to_win += 1
		total_ways *= ways_to_win
	return total_ways


race_data = extract_data('input.txt')
print(calculate_num_winning_options(race_data))


# 2449062
