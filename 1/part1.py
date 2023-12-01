from functions1 import *

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    sum = 0
 
    for line in lines:
        sum += get_calibration_value(line)        
    
    print('The sum of all of the calibration values is {}'.format(sum))