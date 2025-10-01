from Board import Board
import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    @abstractmethod
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    
    def make_move(self, board: Board):
        while True:
            try:
                move = int(input(f'\n{self.name} ({self.symbol}), enter cell (1-9): '))
                if move < 1 or move > 9:
                    print('Invalid cell. Choose a number between 1 and 9!')
                    continue
                row, col = divmod(move - 1, 3)
                if board.is_empty(row, col):
                    board.update((row, col), self.symbol)
                    input("Press Enter to continue...")
                    break
                else:
                    print('Cell already taken. Choose another cell!')
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")

class ComputerPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    
    def make_move(self, board: Board):
        available_cells = board.get_available_cell()
        move = random.choice(available_cells)
        print(f"{self.name} ({self.symbol}) chooses cell {move[0] * 3 + move[1] + 1}")
        board.update(move, self.symbol)
