class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_num = {}
        square_num = {}
        for i, row in enumerate(board):
            row_num = set()
            for j, val in enumerate(row):
                if val !=".":
                    if val in row_num:
                        return False
                    else:
                        row_num.add(val)
                    if j in col_num:
                        if val in col_num[j]:
                            return False
                        else:
                            col_num[j].add(val)
                    else:
                        col_num[j] = set(val)
                    square_id = (i//3)*3+j//3
                    if square_id in square_num:
                        if val in square_num[square_id]:
                            return False
                        else:
                            square_num[square_id].add(val)
                    else:
                        square_num[square_id] = set(val)
        return True
