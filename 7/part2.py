from utils import *
import re

def sort_hands(hands):
    return sorted(hands, key=lambda x: (hand_type(x), hand_strength(x)))

def hand_strength(hand):
    cards,_ = hand
    value = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10}
    return [int(card) if card.isdigit() else value[card] for card in list(cards)]

def hand_type(hand):
    cards,_ = hand

    if cards == 'JJJJJ':
        return 6

    set_of_cards = set(cards)
    if 'J' in set_of_cards:
        set_of_cards.remove('J')
    nr_unique_cards = len(set_of_cards)
   
    match nr_unique_cards:
        case 1: 
            return 6
        case 2:
            max_card_frequencey = max([cards.count(card) for card in set_of_cards]) + cards.count('J')
            if max_card_frequencey == 3:
                return 4
            else:
                return 5
        case 3: 
            max_card_frequencey = max([cards.count(card) for card in set_of_cards]) + cards.count('J')
            if max_card_frequencey == 3:
                return 3
            else:
                return 2
        case 4: 
            return 1
        case 5: 
            return 0
        case _: 
            return 0

def total_winnings(hands):
    hands = sort_hands(hands)
    return sum([(i+1) * int(bid) for i, (cards, bid) in enumerate(hands)])

def parse_input(hands):
    return [hand.split(' ') for hand in hands]

def solution(file_name):
    hands = parse_input(read_input(file_name))
    return total_winnings(hands)

if __name__ == "__main__":
    print(solution("input.txt"))
    