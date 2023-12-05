from utils import *
import re
from part1 import listify_numbers, get_number_of_wins

def extract_wins(card, cards):
    parts = re.split('\||:', card)
    winning_numbers, numbers = [set(listify_numbers(part)) for part in parts[1:]]
    key, wins = int(listify_numbers(parts[0])[0]), len(numbers.intersection(winning_numbers))
    won_cards = cards[key:min(key+wins, len(cards) - 1)]
    print(key, won_cards)

    return won_cards

def count_wins(cards, all_cards):
    if cards == []: return 0

    sum = 0
    for card in cards:
        wins = extract_wins(card, all_cards)
        sum += len(wins) + count_wins(wins, all_cards)
    return sum

def final_scratchcard_count(input_file):
    cards = read_input(input_file)
    return len(cards) + count_wins(cards, cards)

if __name__ == "__main__":
    print(final_scratchcard_count('input.txt'))


