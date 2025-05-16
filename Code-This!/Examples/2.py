def chart(matrix):
    # print the tic-tac-toe board
    # uses a matrix: Tutorials/matrix.md
    chart = f"""
  {matrix[0][0]} | {matrix[0][1]} | {matrix[0][2]}      1 | 2 | 3 
 ---+---+---    ---+---+---
  {matrix[1][0]} | {matrix[1][1]} | {matrix[1][2]}      4 | 5 | 6 
 ---+---+---    ---+---+---
  {matrix[2][0]} | {matrix[2][1]} | {matrix[2][2]}      7 | 8 | 9 
"""
    print(chart)

def checkwin():
    global winner
    # Check rows, columns, and diagonals
    lines = matrix + [list(col) for col in zip(*matrix)] + [
        [matrix[0][0], matrix[1][1], matrix[2][2]],
        [matrix[0][2], matrix[1][1], matrix[2][0]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] != " ":
            winner = line[0]
            return True
    return False

def move(move, player):
    # Check if the move is valid, if it is, place the player's mark
    row, col = divmod(move - 1, 3)
    if matrix[row][col] == " ":
        matrix[row][col] = player
        return True
    return False

# initiallize variables
winner = None
matrix = [[" "] * 3 for _ in range(3)] # 3x3 matrix

# main game loop
while True:
    chart(matrix) # print the board
    # Player 1 move
    while not move(int(input("Player 1 Move: ")), "X"):
        print("Invalid move. Try again.")
    # check for win
    if checkwin():
        break
    chart(matrix) # print the board
    # Player 2 move
    while not move(int(input("Player 2 Move: ")), "O"):
        print("Invalid move. Try again.")
    # check for win
    if checkwin():
        break

chart(matrix) # print the final board
# display the result
if winner:
    print(f"Player {1 if winner == 'X' else 2} wins!")
else:
    print("It's a draw!")