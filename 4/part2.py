from utils import *
import re
from part1 import listify_numbers, get_number_of_wins

def final_scratchcard_count(input_file):
    cards = read_input(input_file)
    card_holder = {}
    sum = 0

    for card in cards:
        card_nr, winning_numbers, numbers = parse_card(card)
        nr_of_wins = len(numbers.intersection(winning_numbers))

        card_instances = 1
        if card_nr in card_holder:
            card_instances += card_holder[card_nr]

        for win in range(card_nr+1, card_nr+1+nr_of_wins):
            if win in card_holder:
                card_holder[win] += card_instances
            else:
                card_holder[win] = card_instances
              
        sum += card_instances
    return sum

def find_numbers(line):
    return [int(n) for n in re.findall(r'\d+', line)]

def parse_card(card):
    parts = re.split('\||:', card)
    card_nr, winning_numbers, numbers = [find_numbers(part) for part in parts]
    return card_nr[0], set(winning_numbers), set(numbers)

if __name__ == "__main__":
    print(final_scratchcard_count('input.txt'))

 
    

