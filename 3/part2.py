import re
from utils import *
from part1 import *

def get_ratio_sum(input):
    lines = read_input(input)

    gear_tracker = {}

    for line_number, line in enumerate(lines):
        numbers = find_numbers(line)
        for number in numbers:
            t, r, b, l = find_trbl_search_area(line_number, line, lines, number)
            for y, search_area in enumerate([line[l:r] for line in lines[t:b]]):
                local_gear_indices = [match.start(0) for match in re.finditer('\*', search_area)]
                global_gear_indices = [(y + t, x + l) for x in local_gear_indices]
                for i in global_gear_indices:
                    if i in gear_tracker: 
                        gear_tracker[i] += [number[0]]
                    else: gear_tracker[i] = [number[0]]

    return sum([gear_numbers[0] * gear_numbers[1] for gear_numbers in gear_tracker.values() if len(gear_numbers) > 1])

if __name__ == "__main__":
    print(get_ratio_sum("input.txt"))





