import numpy as np
import error_checking as error
from colours import bcolours

class Chess():
    def __init__(self):

        self.board = np.array([
            ["-", "A", "B", "C", "D", "E", "F", "G", "H"],
            ['8', 'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
            ['7', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['6', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['5', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['4', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['3', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['1', 'r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        ])

    def move_piece(self, current_cord: str, move_coord: str, player_number: int):
        
        # Error Checking
        if not error.check_valid_coords(current_cord):
            print(bcolours.FAIL + f"Error: Invalid co-ordinate input: {current_cord}" + bcolours.ENDC)
            return False

        if not error.check_valid_coords(move_coord):
            print(bcolours.FAIL + f"Error: Invalid co-ordinate input: {move_coord}" + bcolours.ENDC)
            return False

        if not error.check_valid_move(current_cord, move_coord, player_number, self.board):
            return False
        
        # Move piece
        current_row, current_col = grid_coord_to_index(current_cord)
        move_row, move_col = grid_coord_to_index(move_coord)

        self.board[move_row][move_col] = self.board[current_row][current_col]
        self.board[current_row][current_col] = '0'

        return True

    def reset_board(self):
        self.board = np.array([
            ["-", "A", "B", "C", "D", "E", "F", "G", "H"],
            ['8', 'R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
            ['7', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['6', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['5', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['4', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['3', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['1', 'r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']
        ])

        print("The board has been reset")

    def play(self):
        # Message to terminal
        key = 'Key: R - Rook, N - Knight, B - Bishop, K - King, Q - Queen, P - Pawn.'

        print('\nLowercase is player 1, uppercase is player 2, player 1 goes first.')
        print(key)

        player_number = 1

        while True:
            print(f"\n{self.board}")

            successful_move = False
            print(f"\nPlayer {player_number}'s go.")

            while not successful_move:
                current_coord = input("Choose a piece to move: ")
                move_coord = input("Choose a square to move to: ")

                successful_move = self.move_piece(current_coord, move_coord, player_number)

                if not successful_move:
                    print(f"\nPlayer {player_number} please try again...")

            player_number = 2 if player_number == 1 else 1



def grid_coord_to_num_coord(coord: str):
    """
    Converts a grid co-ordinate into a numeric co-ordinate used to control movement
    """
    coord = coord.upper()

    column = ord(coord[0]) - 64
    row = int(coord[1])

    return (row * 10) + column

def grid_coord_to_index(coord: str):
    """
    Returns a tuple `(row, column)` for a given coordinate in the board matrix
    """
    coord = coord.upper()
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]

    row = row_index[int(coord[1]) - 1]
    column = ord(coord[0]) - 64

    return (row, column)

def num_coord_to_index(num_coord: int):
    
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]

    row = row_index[(num_coord // 10) - 1]
    column = num_coord % 10

    return (row, column)