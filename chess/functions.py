import numpy as np


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
        
        current_cord = current_cord.upper()
        move_coord = move_coord.upper()

        #Error Checking
        if not check_valid_coords(current_cord):
            print(f"Error: Invalid co-ordinate input: {current_cord}", end = "\n\n")
            return False

        if not check_valid_coords(move_coord):
            print(f"Error: Invalid co-ordinate input: {move_coord}", end = "\n\n")
            return False
        
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
        print(key, end = "\n")

        player_number = 1

        while True:
            print(f"\n{self.board}", end = "\n\n")

            successful_move = False

            while not successful_move:
                current_coord = input(f"Player {player_number} - Choose a peice to move: ")
                move_coord = input(f"Player {player_number} - Choose a square to move to: ")

                successful_move = self.move_piece(current_coord, move_coord, player_number)           

            player_number = 2 if player_number == 1 else 1



def grid_coord_to_num_coord(coord: str):
    column = ord(coord[0]) - 64
    row = int(coord[1])

    return (row * 10) + column

def grid_coord_to_index(coord: str):
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]
    
    row = row_index[int(coord[1]) - 1]
    column = ord(coord[0]) - 64

    return (row, column)

def check_valid_coords(coord: str):
    if len(coord) != 2:
        return False
    if not coord[0].isalpha() or not coord[1].isdigit():
        return False
    if ord(coord[0]) - 65 < 0 or ord(coord[0]) - 65 > 7:
        return False
    if int(coord[1]) < 0 or int(coord[1]) > 8:
        return False  

    return True



