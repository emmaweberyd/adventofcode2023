import re

def max_cube_count(game, color):
    max_cube_count = 0
    for match in re.finditer(rf"(?P<count>\d+) {color}", game):
        max_cube_count = max(max_cube_count, int(match.group('count')))
    return max_cube_count

def is_possible(game):
    if (max_cube_count(game, 'red') > 12): return False
    if (max_cube_count(game, 'green') > 13): return False
    if (max_cube_count(game, 'blue') > 14): return False
    return True

def sum_ids_of_possible_games(games):
    sum = 0
    for (i, game) in enumerate(games):
        if (is_possible(game)):
            sum += i+1 
    return sum

def get_id_sum_of_possible_games(game_input_file):
    with open(game_input_file) as f:
        games = f.readlines()
    return sum_ids_of_possible_games(games)

if __name__ == "__main__":
    sum = get_id_sum_of_possible_games('input.txt')
    print('The sum of the IDs of the possible games is {}'.format(sum))