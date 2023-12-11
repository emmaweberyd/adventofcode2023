from utils import *
import numpy as np

def get_prev_history_value(sequence):
    diff_sequence = np.diff(sequence)
    return sequence[0] if set(sequence) == set(sequence[0:1]) else sequence[0] - get_prev_history_value(diff_sequence)

def get_history_sum(file_name):
    sequences = parse_input(file_name)
    return sum([get_prev_history_value(sequence) for sequence in sequences])

if __name__ == "__main__":
    print(get_history_sum('input.txt'))