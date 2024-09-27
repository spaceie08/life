from bitarray import bitarray

class life:
    
    """ A python Implementation of Game of Life.
    As part of the big Geo data course
    Rules:
        - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        - Any live cell with two or three live neighbours lives on to the next generation.
        - Any live cell with more than three live neighbours dies, as if by overpopulation.
        - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
    
    def __init__(self, filename: str):
        """ Create a game of life object.
        Args:
        filename: Input file name.
        Raises:
            Exception: if input data is invalid.
        """
        self.filename = filename
        self.grid = []
        with open(filename) as f:
            self.w, self.h = map(int, f.readline().split(maxsplit=1))
            
            for y in range(self.h + 2):
                self.grid.append(bitarray(self.w + 2))
                self.grid[y].setall(0)
            
            for no, line in enumerate(f):
                try:
                    y, x = map(int, line.split(maxsplit=1))
                    if y < 0 or x < 0:
                        raise ValueError
                except ValueError:
                    raise Exception(f"Invalid cell on line {no + 2}.")
                self.grid[y + 1][x + 1] = 1 
    def tick(self, num_generations: int = 1):
        """
        Applies the rules of Game of Life for the specified number of Generations.

        Args:
            num_generations: Number of the generation.
        """
        for i in range(num_generations):
            for y, row in enumerate(self.grid[1: -1], start=1):
                curr = [0] * (self.w + 2)
                for x, cell in enumerate(row[1:-1], start=1):
                    # Count the number of live neighbors
                    count = (self.grid[y-1][x-1] + self.grid[y-1][x] + self.grid[y-1][x+1] +
                             self.grid[y][x-1] + self.grid[y][x+1] +
                             self.grid[y+1][x-1] + self.grid[y+1][x] + self.grid[y+1][x+1])
                    # Apply the rules of life
                    curr[x] = 1 if count == 3 or (cell and count == 2) else 0
                
                if y > 1:
                    self.grid[y - 1] = prev  # Update the previous row
                prev = curr
            self.grid[self.h] = curr  # Update the last row
    
    def export_grid(self, output_filename: str):
        """
        Exports the current state of the grid to a text file in the same format as the input file.
        Args:
            output_filename: The output file name where the grid will be saved.
        """
        with open(output_filename, 'w') as f:
            # Write the grid dimensions (width and height)
            f.write(f"{self.w} {self.h}\n")
            
            # Loop through the grid and write coordinates of live cells
            for y in range(1, self.h + 1):  # Skip border rows
                for x in range(1, self.w + 1):  # Skip border columns
                    if self.grid[y][x] == 1:  # If the cell is alive
                        f.write(f"{y-1} {x-1}\n")  # Output zero-indexed coordinates

