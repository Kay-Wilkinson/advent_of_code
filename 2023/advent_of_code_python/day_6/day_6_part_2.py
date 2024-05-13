"""
The brute force approach of part 1 will be too slow for this iteration of the puzzle. 
Using binary search to find the max and min hold times necessary to beat the record and then
calculating the number of possible wins within that range.
"""

def extract_data(input_data):
	with open(input_data, 'r') as file:
		race_stats = [line.strip().split() for line in file]
		print(race_stats)
		kerned_times = [str(x) for x in race_stats[0][1:]]
		times = ''.join(kerned_times)
		distance = [str(x) for x in race_stats[1][1:]]
		distances = ''.join(distance)
		return int(times), int(distances)

def calculate_num_winning_options(time, record):
    # Binary search for minimum and maximum hold time
    def search_for_hold_time(low, high, condition):
        while low < high:
            mid = (low + high) // 2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        return low

    # Condition to check if the distance is greater than the record
    def is_distance_greater(hold_time):
        return hold_time * (time - hold_time) > record

    # Finding the minimum hold time that beats the record
    min_hold_time = search_for_hold_time(0, time, is_distance_greater)

    # Finding the maximum hold time that beats the record
    max_hold_time = search_for_hold_time(min_hold_time, time, lambda ht: not is_distance_greater(ht)) - 1

    # Calculate number of winning options
    ways_to_win = max(0, max_hold_time - min_hold_time + 1)
    return ways_to_win


times, distances = extract_data('input.txt')
wins = calculate_num_winning_options(times, distances)
print(wins)
