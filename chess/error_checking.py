import functions as func


def check_valid_coords(coord: str):
    coord = coord.upper()

    if len(coord) != 2:
        return False
    if not coord[0].isalpha() or not coord[1].isdigit():
        return False
    if ord(coord[0]) - 65 < 0 or ord(coord[0]) - 65 > 7:
        return False
    if int(coord[1]) < 0 or int(coord[1]) > 8:
        return False  

    return True

def check_valid_move(current_coord: str, move_coord: str, player_number: int, board):

    current_row, current_col = func.grid_coord_to_index(current_coord)
    move_row, move_col = func.grid_coord_to_index(move_coord)

    current_num = func.grid_coord_to_num_coord(current_coord)
    move_num = func.grid_coord_to_num_coord(move_coord)

    piece_bool = True if player_number == 1 else False

    if board[current_row][current_col] == '0':
        print(f"Error: No piece found on square {current_coord}.")
        return False

    if board[current_row][current_col].islower() != piece_bool:
        player1_error = "Error: Player 1 uses lowercase pieces, not uppercase."
        player2_error = "Error: Player 2 uses uppercase pieces, not lowercase."

        print(player1_error) if piece_bool else print(player2_error)
        return False
    
    piece_type = board[current_row][current_col]
    target_square = board[move_row][move_col]

    if not check_valid_movement(current_num, move_num, piece_type, target_square, player_number):
        print(f"Error: Cannot move {piece_type}({current_coord} square) to {move_coord} square.")
        return False

    return True

def check_valid_movement(current_num: int, move_num: int, piece_type: str, target_square: str, player_num: int):
    
    diagonals = [9, 11]
    lateral_vertical = [1, 2, 3, 4, 5, 6, 7, 10]
    knight = [8, 12, 19, 21]
    king = [1, 9, 10, 11]

    piece_type = piece_type.lower()
    square_difference = abs(current_num - move_num)

    if piece_type == 'k' and square_difference not in king:
        return False
    elif piece_type == 'q' and not [1 for i in (diagonals + lateral_vertical) if square_difference % i == 0]:
        return False
    elif piece_type == 'r' and not [1 for i in lateral_vertical if square_difference % i == 0]:
        return False
    elif piece_type == 'n' and not [1 for i in knight if square_difference % i == 0]:
        return False
    elif piece_type == 'b' and not [1 for i in diagonals if square_difference % i == 0]:
        return False
    elif piece_type == 'p' and not valid_pawn_move(current_num, move_num, target_square, player_num):
        return False
    
    return True

def valid_pawn_move(current_num: int, move_num: int, target_square: str, player_num: int):
    
    pawn = [10]
    pawn_start = [10, 20]
    pawn_taking = [9, 11]

    square_difference = current_num - move_num

    # Set player respective variables
    if player_num == 1:
        square_difference *= -1
        starting_position = True if (current_num > 20 and current_num < 29) else False
    elif player_num == 2:
        starting_position = True if (current_num > 70 and current_num < 79) else False

    print(square_difference, starting_position)

    if target_square == '0' and starting_position and square_difference not in pawn_start:
        return False
    elif target_square == '0' and not starting_position and square_difference not in pawn:
        return False
    elif target_square != '0' and square_difference not in pawn_taking:
        return False
    
    return True