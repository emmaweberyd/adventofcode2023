from utils import *
from part1 import get_distance, nr_of_ways_to_win
import re

def find_number(line):
    return int(line.split(':')[1].replace(' ', ''))

def solution(file_name):
    time, distance = read_input(file_name)
    race = find_number(time), find_number(distance)
    return nr_of_ways_to_win(race)

if __name__ == "__main__":
    print(solution("input.txt"))
    