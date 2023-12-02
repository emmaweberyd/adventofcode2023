valid_digits = ['1', '2', '3', '4', '5', '6', '7', '8','9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

word_to_digit = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def find_first_digit(input):
    smallest_index, first_digit = len(input), 0 

    for digit in valid_digits:
        found_index = input.find(digit)
        if (found_index >= 0 and found_index < smallest_index): 
            smallest_index = found_index
            first_digit = digit

    return word_to_digit[first_digit]

def find_last_digit(input):
    highest_index, last_digit = 0, 0

    for digit in valid_digits:
        found_index = input.rfind(digit)
        if (found_index >= 0 and found_index >= highest_index):
            print(found_index)
            highest_index = found_index
            last_digit = digit

    return word_to_digit[last_digit]

def get_calibration_value(input):
    return int(find_first_digit(input) + find_last_digit(input))

def get_calibration_sum(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        sum += get_calibration_value(line)
    return sum
 