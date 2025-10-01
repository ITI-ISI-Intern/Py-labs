class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    
    def display(self):
        print(self)
    
    def update(self, position, symbol):
        row, col = position
        self.grid[row][col] = symbol
    
    def check_winner(self):
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != ' ':
                return self.grid[i][0]

            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != ' ':
                return self.grid[0][i]
        
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return self.grid[0][2]
        
        return None
    
    def is_empty(self, row, col):
        return self.grid[row][col] == ' '
    
    def is_full(self):
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    return False
        return True
    
    def get_available_cell(self):
        return [(i, j) for i in range(3) for j in range(3) if self.is_empty(i, j)]
    
    def dipslay_available_cells(self):
        available = self.get_available_cell()
        available_cells = []
        for cell in available:
            cell_number = cell[0] * 3 + cell[1] + 1
            available_cells.append(str(cell_number))
        print("\nAvailable cells: " + ", ".join(available_cells))
        
    def __str__(self):
        rows = []
        for row in self.grid:
            rows.append(f' {row[0]} | {row[1]} | {row[2]} ')
        return "\n-----------\n".join(rows)
