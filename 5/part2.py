from utils import *
from part1 import convert, find_numbers
import numpy as np
import re

INF = 2**63 - 1

def intersection(source_range, map_range):
    source_start, source_end = source_range
    destination_start, map_start, map_end = map_range

    if source_start <= map_end and source_end >= map_start:
        offset = (destination_start-map_start)
        return np.array([max(source_start, map_start) + offset, min(source_end, map_end)  + offset])
    return np.array([])

def get_almanac_from_file(file_name):
    with open(file_name, 'r') as file:
        data = file.read()

    parts = [i.strip().splitlines() for i in re.split(r"[^\d+\n ]", data) if i.strip() != '']

    almanac = []
    for part in parts:
        conversion_map =[]
        for piece in part:
            conversion_map.append(find_numbers(piece))
        almanac.append(conversion_map)
    
    return np.reshape(np.array(almanac[0][0]), (-1,2)).astype(int), almanac[1:]


def add_missing_ranges(almanac): 
    new_almanac = []
    for i, conversion_map in enumerate(almanac):
        conversion_map.sort(key=lambda x: x[1])

        new_conversion_map = []
        if conversion_map[0][1] != 0:
            new_conversion_map.append([0, 0, conversion_map[0][1]-1])

        for j, map_piece in enumerate(conversion_map):
            if j+1 == len(conversion_map):
                new_conversion_map.append([map_piece[2]+1, map_piece[2]+1, INF])
            elif map_piece[2]+1 != conversion_map[j+1][1]:
                new_conversion_map.append([map_piece[2]+1, map_piece[2]+1, conversion_map[j+1][1]-1])
                
        new_almanac.append(new_conversion_map + conversion_map)
    return new_almanac

def find_lowest_location_numner(file_name):
    sources, almanac = get_almanac_from_file(file_name)

    sources = [[source_start, source_start+source_count-1] for source_start, source_count in sources]

    alm = []
    for conversion_map in almanac:
        alm.append([[int(destination_start), int(source_start), int(source_start)+int(count)-1] for (destination_start, source_start, count) in conversion_map])

    almanac = add_missing_ranges(alm)
    
    for conversion_map in almanac:
        new_sources = []
        for source_range in sources:
            for map_piece in conversion_map:
                intersect = intersection(source_range, map_piece)
                if intersect.shape != (0,): 
                    new_sources.append(intersect) 
        sources = new_sources
    
    return min(np.array(sources).flatten())


if __name__ == "__main__":
    print(find_lowest_location_numner("input.txt"))