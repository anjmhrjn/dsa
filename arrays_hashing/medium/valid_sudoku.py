"""
You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Example 1:
Input: board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
"""
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        board_num_count = [[0] * 9] * 9
        board_count = {}
        section = 0
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                element = board[i][j]
                
                if element != ".":
                    # check row
                    row_key = "row"+str(i+1)+element
                    if board_count.get(row_key, 0) == 0:
                        board_count[row_key] = 1
                    else:
                        print("row duplicate for: " + element)
                        return False

                    # check column
                    col_key = "col"+str(j+1)+element
                    if board_count.get(col_key, 0) == 0:
                        board_count[col_key] = 1
                    else:
                        print("column duplicate for: " + element)
                        return False
                    
                    # check box
                    box_number = section + int(j/3)
                    box_key = "box"+str(box_number)+element
                    if board_count.get(box_key, 0) == 0:
                        board_count[box_key] = 1
                    else:
                        return False
            if (i+1)%3 == 0:
                section += 3
        return True
    
# simpler solution
class SimplerSolution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".": 
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
            
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True



from collections import defaultdict
class SingleLoopSolution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
                

        