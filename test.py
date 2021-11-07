def grid_coord_to_index(coord: str):
    """
    Returns a tuple `(row, column)` for a given coordinate in the board matrix
    """
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]

    row = row_index[int(coord[1]) - 1]
    column = ord(coord[0]) - 96

    return (row, column)

print(grid_coord_to_index('d4'))