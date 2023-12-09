def read_input(file_name):
    with open(file_name) as f:
        return f.read().splitlines()

def find_numbers(line):
    return [int(n) for n in line.split(' ')]

def parse_input(file_name):
    lines = []
    for line in read_input(file_name):
        lines.append(find_numbers(line))
    return lines