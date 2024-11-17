import numpy as np 
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols= defaultdict(set)
        rows= defaultdict(set)
        square= defaultdict(set)
        sdk_length= len(board)
        boards_numbers= sdk_length/np.sqrt(sdk_length)
        for i in range(sdk_length):
            for j in range(sdk_length):
                if board[i][j]==".":
                    continue
                if board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j] in square[(i//boards_numbers, j//boards_numbers)]:
                                       
                    return False

                else:
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    square[(i//boards_numbers, j//boards_numbers)].add(board[i][j])

        return True