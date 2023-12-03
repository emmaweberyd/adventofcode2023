import re
from utils import *

def find_numbers(line):
    return [(int(match.group(0)),int(match.start(0)), int(match.end(0))) for match in re.finditer(r"\d+", line)]

def is_part_number(search_area):
    return bool(re.search(r"[^\d.]", search_area))

def find_trbl_search_area(line_number, line, lines, number):
    return max(line_number - 1, 0), min(number[2] + 1, len(line) - 1), min(line_number + 1, len(lines) - 1) + 1, max(number[1] - 1, 0)

def sum_of_part_numbers(input_file):
    lines = read_input(input_file)

    sum = 0

    for line_number, line in enumerate(lines):
        numbers = find_numbers(line)
        for number in numbers:
            t, r, b, l = find_trbl_search_area(line_number, line, lines, number)
            search_area = ''.join([line[l:r] for line in lines[t:b]])
            if is_part_number(search_area): sum += number[0]
    return sum

if __name__ == "__main__":
    print(sum_of_part_numbers('input.txt'))