from utils import *
import re

def wins_to_points(nr_of_wins):
    if nr_of_wins == 0: return 0
    return 2**(nr_of_wins-1)

def extract_numbers(card):
    parts = re.split('\||:', card)[1:]
    return listify_numbers(parts[0]), listify_numbers(parts[1])

def listify_numbers(number_string):
    return re.findall(r'\d+', number_string)

def get_number_of_wins(card):
    winning_numbers, numbers = extract_numbers(card)
    return len([winning_number for winning_number in  winning_numbers if winning_number in numbers])

def points(card):
    return wins_to_points(get_number_of_wins(card))

def total_points(file_name):
    cards = read_input(file_name)
    return sum([points(card) for card in cards])

if __name__ == "__main__":
    print(total_points('input.txt'))