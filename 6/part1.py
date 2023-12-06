from utils import *
import re

def get_distance(race_duration, button_hold):
    travel_time = race_duration - button_hold
    velocity = button_hold
    return travel_time * velocity

def nr_of_ways_to_win(race):
    time, record_distance = race
    return len([result for result in [get_distance(time, millisecond) for millisecond in list(range(time+1))] if result > record_distance])

def find_numbers(line):
    return [int(n) for n in re.findall(r'\d+', line)]

def solution(file_name):
    times, distances = read_input(file_name)

    races = list(zip(find_numbers(times), find_numbers(distances)))

    product = 1
    for race in races:
        product *= nr_of_ways_to_win(race)
    return product

if __name__ == "__main__":
    print(solution("input.txt"))
    