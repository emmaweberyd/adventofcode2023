import numpy as np

class PathSolver:
    def __init__(self, file_name):
        self.grid = self.read_input(file_name)

    def read_input(self, file_name):
        with open(file_name) as f:
            return np.array([list(line) for line in f.read().splitlines()])

    def find_start_tile(self):
        return Tile('S', tuple(np.argwhere(self.grid == 'S')[0]))

    def nr_of_steps(self):
        current_tile = self.find_start_tile()
        previous_tile = None
        steps = 0

        while True:
            next_tile = self.find_next_tile(current_tile, previous_tile)
            previous_tile = current_tile
            current_tile = next_tile
            steps += 1
            if next_tile.shape == 'S':
                break

        return int(steps / 2)
    
    def find_next_tile(self, tile, previous_tile = None):
        adjacent_tiles = self.find_adjacent_tiles(tile)
        if type(previous_tile) == type(None):
            return adjacent_tiles[0]
        return [t for t in adjacent_tiles if t != previous_tile][0]

    def find_adjacent_tiles(self, tile):
        adjacent_tiles = []
        if tile.y-1 >= 0 and tile.shape in ['|', 'L', 'J', 'S'] and self.grid[tile.y-1, tile.x] in ['|', 'F', '7', 'S']: #N
            adjacent_tiles.append(Tile(self.grid[tile.y-1, tile.x], (tile.y-1, tile.x)))
        if tile.y+1 <= len(self.grid)-1 and tile.shape in ['|', 'F', '7', 'S'] and self.grid[tile.y+1, tile.x] in ['|', 'L', 'J', 'S']: #S
            adjacent_tiles.append(Tile(self.grid[tile.y+1, tile.x], (tile.y+1, tile.x)))
        if tile.x-1 >= 0 and tile.shape in ['-', '7', 'J', 'S'] and self.grid[tile.y, tile.x-1] in ['-', 'L', 'F', 'S']: #W
            adjacent_tiles.append(Tile(self.grid[tile.y, tile.x-1], (tile.y, tile.x-1)))
        if tile.x+1 <= len(self.grid[0])-1 and tile.shape in ['-', 'L', 'F', 'S'] and self.grid[tile.y, tile.x+1] in ['-', 'J', '7', 'S']: #E
            adjacent_tiles.append(Tile(self.grid[tile.y, tile.x+1], (tile.y, tile.x+1)))
        return adjacent_tiles

class Tile:
    def __init__(self, shape, index):
        self.shape, self.y, self.x = shape, index[0], index[1]

    def __repr__(self):
        return f"({self.shape}: [{self.y}, {self.x}])"
    
    def __str__(self):
        return f"({self.shape}: [{self.y}, {self.x}])"
    
    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

if __name__ == "__main__":
    print(PathSolver('input.txt').nr_of_steps())



