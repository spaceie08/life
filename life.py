from bitarray import bitarray
@profile
def read_grid(filename):
    grid = []
    with open(filename) as f:
        w, h = map(int, f.readline().split(maxsplit=1))
        
        for y in range(h):
            grid.append(bitarray(w))
        
        for no, line in enumerate(f):
            try:
                y, x = map(int, line.split(maxsplit=1))

                if y < 0 or x < 0:
                    raise ValueError

            except ValueError:
                raise Exception(f"Invalid cell on line {no + 2}.")

            grid[y][x] = 1

    return grid

def tick(grid):
    h, w = len(grid), len(grid[0])

    nextgrid = []
    for y in range(h):
        nextgrid.append(bitarray(w))

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            count = 0
            if y > 0:
                count += grid[y-1][x-1] if x > 0 else 0
                count += grid[y-1][x]
                count += grid[y-1][x+1] if x < w - 1 else 0
            count += grid[y][x-1] if x > 0 else 0
            count += grid[y][x+1] if x < w - 1 else 0
            if y < h - 1:
                count += grid[y+1][x-1] if x > 0  else 0
                count += grid[y+1][x] 
                count += grid[y+1][x+1] if x < w - 1 else 0

            nextgrid[y][x] = 1 if count == 3 or (cell and count == 2) else 0

    return nextgrid

filename = "input_5x5.txt"

grid = read_grid(filename)
# print(grid)

nextgrid=tick(grid)
print(nextgrid)






















