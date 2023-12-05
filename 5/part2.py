from utils import *
from part1 import convert, find_numbers
import numpy as np
import re

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
    
    source_map = np.reshape(np.array(almanac[0][0]), (-1,2)).astype(int)
    sources = []
    for source in source_map:
        sources += [*range(source[0],source[0]+source[1])]
    
    for part in almanac[1:]:
        for i, source in enumerate(sources):
            next_source = convert(source, part)
            sources[i] = next_source

    return min(sources)

if __name__ == "__main__":
    print(find_lowest_location_numner("input.txt"))