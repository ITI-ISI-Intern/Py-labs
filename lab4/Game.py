import random
from Board import Board
from player import ComputerPlayer, HumanPlayer

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_turn = 0

    def setup(self):
        print("1) Play with human")
        print("2) Play with computer")

        while True:
            try:
                choice = int(input("Choose mode (1 or 2): "))
                if choice == 1:
                    while True:
                        player1 = input("Enter Player 1 name: ").strip()
                        if not player1.isalpha():
                            print("Please enter a valid name!")
                            continue
                        self.players.append(HumanPlayer(player1, "X"))
                        break

                    while True:
                        player2 = input("Enter Player 2 name: ").strip()
                        if not player2.isalpha():
                            print("Please enter a valid name!")
                            continue
                        self.players.append(HumanPlayer(player2, "O"))
                        break
                    break

                elif choice == 2:
                    while True:
                        player = input("Enter your name: ").strip()
                        if not player.isalpha():
                            print("Please enter a valid name!")
                            continue
                        break

                    symbol = ""
                    while symbol not in ("X", "O"):
                        symbol = input("Choose your symbol (X/O): ").upper()

                    comp_symbol = "O" if symbol == "X" else "X"
                    human_first = random.choice([True, False])

                    if human_first:
                        self.players.append(HumanPlayer(player, symbol))
                        self.players.append(ComputerPlayer("Computer", comp_symbol))
                    else:
                        self.players.append(ComputerPlayer("Computer", comp_symbol))
                        self.players.append(HumanPlayer(player, symbol))
                    break

                else:
                    print("Invalid choice, please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")

    def play(self):
        self.setup()
        while True:
            self.board.display()
            current_player = self.players[self.current_turn]
            self.board.dipslay_available_cells()
            current_player.make_move(self.board)

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"Congratulations,{current_player.name} wins!")
                break
            elif self.board.is_full():
                self.board.display()
                print("It's a draw!")
                break

            self.current_turn = 1 - self.current_turn

if __name__ == "__main__":
    game = Game()
    game.play()
