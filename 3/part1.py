import re

def find_numbers(line):
    return [(int(match.group(0)),int(match.start(0)), int(match.end(0))) for match in re.finditer(r"\d+", line)]

def is_part_number(search_area):
    return bool(re.search(r"[^\d.]", search_area))


def sum_of_part_numbers(input_file):
    with open(input_file) as f:
        lines = f.read().splitlines()

    sum = 0

    for line_number, line in enumerate(lines):
        numbers = find_numbers(line)
        for number in numbers:
            left_limit = max(number[1] - 1, 0)
            right_limit = min(number[2] + 1, len(line) - 1)
            top_limit = max(line_number - 1, 0)
            bottom_limit = min(line_number + 1, len(lines) - 1) + 1
            search_area = ''.join([line[left_limit:right_limit] for line in lines[top_limit:bottom_limit]])
            if is_part_number(search_area): sum += number[0]
    return sum

if __name__ == "__main__":
    print(sum_of_part_numbers('input.txt'))