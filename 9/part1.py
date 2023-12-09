from utils import *
import numpy as np

def get_next_history_value(sequence):
    return sequence[-1] + get_next_in_diff_sequence(sequence)

def get_next_in_diff_sequence(sequence):
    diff_sequence = np.diff(sequence)
    return 0 if np.all(diff_sequence==0) else diff_sequence[-1] + get_next_in_diff_sequence(diff_sequence)

def get_history_sum(file_name):
    sequences = parse_input(file_name)
    return sum([get_next_history_value(sequence) for sequence in sequences])

if __name__ == "__main__":
    print(get_history_sum('input.txt'))

