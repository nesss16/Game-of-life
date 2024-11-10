class Grid :
    def __init__(self, size=50):
        self.size = size
        self.cells = [[Cell() for i in range(size)] for j in range(size)]

    def randomize(self):
        for row in self.cells:
            for cell in row:
                cell.alive = random.choice([True, False])

    def update(self):
        new_cells = [[Cell() for i in range(self.size)] for j in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                live_neighbors = self.count_live_neighbors(row, col)
                if self.cells[row][col].is_alive():
                    if live_neighbors in [2, 3]:
                        new_cells[row][col].make_alive()
                    else:
                        new_cells[row][col].make_dead()
                else:
                    if live_neighbors == 3:
                        new_cells[row][col].make_alive()
        self.cells = new_cells

    def count_live_neighbors(self, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.size and 0 <= c < self.size:
                if self.cells[r][c].is_alive():
                    count += 1
        return count
