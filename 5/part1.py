from utils import *
import re

def convert(source, map):
    for line in map:
        source_range = [*range(int(line[1]), int(line[1])+int(line[2]))]
        destination_range = [*range(int(line[0]), int(line[0])+int(line[2]))]
        source_to_destination = dict(zip(source_range, destination_range))
        if source in source_to_destination:
            return source_to_destination[source]
    return source

def find_numbers(line):
    return re.findall(r'\d+', line)

def get_seeds(almanac):
    return find_numbers(almanac[0])

def find_lowest_location_numner(file_name):
    with open(file_name, 'r') as file:
        data = file.read()

    parts = [i.strip().splitlines() for i in re.split(r"[^\d+\n ]", data) if i.strip() != '']

    almanac = []
    for part in parts:
        convertion_map =[]
        for piece in part:
            convertion_map.append(find_numbers(piece))
        almanac.append(convertion_map)
    
    sources = almanac[0][0]
    for part in almanac[1:]:
        for i, source in enumerate(sources):
            next_source = convert(int(source), part)
            sources[i] = next_source

    return min(sources)

if __name__ == "__main__":
    print(find_lowest_location_numner("test_input.txt"))
    
