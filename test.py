def num_coord_to_index(num_coord: int):
    
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]

    row = row_index[num_coord // 10]
    column = num_coord % 10

    return (row, column)

print(num_coord_to_index(84))