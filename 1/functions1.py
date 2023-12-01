def get_first_digit(str):
    for c in str:
        if c.isnumeric():
            return c

def get_last_digit(str): 
    return get_first_digit(str[::-1])

def get_calibration_value(str):
    return int(get_first_digit(str) + get_last_digit(str))