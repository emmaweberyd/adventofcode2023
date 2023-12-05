from utils import *
import re

def convert(source, map):
    for destination_range_start, source_range_start, range_length in map:
        if source <= int(source_range_start) + int(range_length) - 1 and source >= int(source_range_start):
            return int(destination_range_start) + source - int(source_range_start)
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
        conversion_map =[]
        for piece in part:
            conversion_map.append(find_numbers(piece))
        almanac.append(conversion_map)
    
    sources = almanac[0][0]
    for part in almanac[1:]:
        for i, source in enumerate(sources):
            next_source = convert(int(source), part)
            sources[i] = next_source

    return min(sources)

if __name__ == "__main__":
    print(find_lowest_location_numner("input.txt"))
    
