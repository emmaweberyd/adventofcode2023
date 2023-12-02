from part1 import *

def get_minimum_set_of_cubes(game):
    return max_cube_count(game, 'red'), max_cube_count(game, 'green'), max_cube_count(game, 'blue')

def get_minimum_cube_set_power(game):
    red, green, blue = get_minimum_set_of_cubes(game)
    return red * green * blue

def sum_of_minimum_cub_set_powers(game_file):
    with open(game_file) as f:
        games = f.readlines()

    return sum([get_minimum_cube_set_power(game) for game in games])

if __name__ == "__main__":
    print(sum_of_minimum_cub_set_powers('input.txt'))
