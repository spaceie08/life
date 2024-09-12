from bitarray import bitarray

def read_grid(filename):
    grid = []
    with open(filename) as f:
        w, h = map(int, f.readline().split(maxsplit=1))
        
        for y in range(h+2):
            grid.append(bitarray(w+2))
        
        for no, line in enumerate(f):
            try:
                y, x = map(int, line.split(maxsplit=1))

                if y < 0 or x < 0:
                    raise ValueError

            except ValueError:
                raise Exception(f"Invalid cell on line {no + 2}.")

            grid[y+1][x+1] = 1

    return grid

@profile
def tick(grid):
    h, w = len(grid)-2, len(grid[0])-2

    nextgrid = []
    for y in range(h+2):
        nextgrid.append(bitarray(w+2))

    for y, row in enumerate(grid[1:-1]):
        for x, cell in enumerate(row[1:-1]):
            count = + grid[y][x]  + grid[y][x+1]  +grid[y][x+2]   + grid[y+1][x]   + grid[y+1][x+2]   + grid[y+2][x]  + grid[y+2][x+1]  + grid[y+2][x+2]
            nextgrid[y+1][x+1] = 1 if count == 3 or (cell and count == 2) else 0

    return nextgrid

filename = "input_5x5.txt"

grid = read_grid(filename)
print(grid)

nextgrid=tick(grid)
print(nextgrid)






















