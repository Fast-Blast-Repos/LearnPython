def chart(matrix):
    chart = f"""
  {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]} || {matrix[0][3]} | {matrix[0][4]} | {matrix[0][5]} || {matrix[0][6]} | {matrix[0][7]} | {matrix[0][8]}      1 | 2 | 3 || 4 | 5 | 6 || 7 | 8 | 9
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]} || {matrix[1][3]} | {matrix[1][4]} | {matrix[1][5]} || {matrix[1][6]} | {matrix[1][7]} | {matrix[1][8]}      10| 11| 12|| 13| 14| 15|| 16| 17| 18
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]} || {matrix[2][3]} | {matrix[2][4]} | {matrix[2][5]} || {matrix[2][6]} | {matrix[2][7]} | {matrix[2][8]}      19| 20| 21|| 22| 23| 24|| 25| 26| 27
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[3][0]} | {matrix[3][1]} | {matrix[3][2]} || {matrix[3][3]} | {matrix[3][4]} | {matrix[3][5]} || {matrix[3][6]} | {matrix[3][7]} | {matrix[3][8]}      28| 29| 30|| 31| 32| 33|| 34| 35| 36
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[4][0]} | {matrix[4][1]} | {matrix[4][2]} || {matrix[4][3]} | {matrix[4][4]} | {matrix[4][5]} || {matrix[4][6]} | {matrix[4][7]} | {matrix[4][8]}      37| 38| 39|| 40| 41| 42|| 43| 44| 45
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[5][0]} | {matrix[5][1]} | {matrix[5][2]} || {matrix[5][3]} | {matrix[5][4]} | {matrix[5][5]} || {matrix[5][6]} | {matrix[5][7]} | {matrix[5][8]}      46| 47| 48|| 49| 50| 51|| 52| 53| 54
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[6][0]} | {matrix[6][1]} | {matrix[6][2]} || {matrix[6][3]} | {matrix[6][4]} | {matrix[6][5]} || {matrix[6][6]} | {matrix[6][7]} | {matrix[6][8]}      55| 56| 57|| 58| 59| 60|| 61| 62| 63
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[7][0]} | {matrix[7][1]} | {matrix[7][2]} || {matrix[7][3]} | {matrix[7][4]} | {matrix[7][5]} || {matrix[7][6]} | {matrix[7][7]} | {matrix[7][8]}      64| 65| 66|| 67| 68| 69|| 70| 71| 72
 ---+---+---++---+---+---++---+---+---    ---+---+---++---+---+---++---+---+---
  {matrix[8][0]} | {matrix[8][1]} | {matrix[8][2]} || {matrix[8][3]} | {matrix[8][4]} | {matrix[8][5]} || {matrix[8][6]} | {matrix[8][7]} | {matrix[8][8]}      73| 74| 75|| 76| 77| 78|| 79| 80| 81
"""
    print(chart)

def generate_sudoku():
    # Generate a valid Sudoku puzzle with more empty cells
    import random

    def is_valid(matrix, row, col, num):
        # Check if num is not in the current row, column, and 3x3 box
        for i in range(9):
            if matrix[row][i] == num or matrix[i][col] == num:
                return False
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if matrix[i][j] == num:
                    return False
        return True

    def fill_sudoku(matrix):
        # Fill the Sudoku grid recursively
        for row in range(9):
            for col in range(9):
                if matrix[row][col] == 0:
                    for num in random.sample(range(1, 10), 9):
                        if is_valid(matrix, row, col, num):
                            matrix[row][col] = num
                            if fill_sudoku(matrix):
                                return True
                            matrix[row][col] = 0
                    return False
        return True

    # Initialize an empty 9x9 grid
    matrix = [[0 for _ in range(9)] for _ in range(9)]
    fill_sudoku(matrix)

    # Create a copy of the completed Sudoku as the solution
    solution = [row[:] for row in matrix]

    # Remove numbers to create a puzzle
    for _ in range(random.randint(40, 60)):  # Randomly remove between 40 and 60 cells
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        matrix[row][col] = ' '  # Use a space to represent an empty cell

    return matrix, solution

generated_sudoku = generate_sudoku()
solution = generated_sudoku[1]
matrix = generated_sudoku[0]
chart(matrix)

while True:
    move = int(input("Enter your move (1-81): "))
    row, col = divmod(move - 1, 9)
    if matrix[row][col] == ' ':
        num = int(input("Enter the number (1-9): "))
        if solution[row][col] == num:
            matrix[row][col] = num
            chart(matrix)
            if all(cell != ' ' for row in matrix for cell in row):
                print("Congratulations! You've solved the Sudoku!")
                break
        else:
            print("Incorrect number. Try again.")
    else:
        print("Cell already filled. Try again.")