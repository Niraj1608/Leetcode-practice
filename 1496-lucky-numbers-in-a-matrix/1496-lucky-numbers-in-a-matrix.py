class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        row,col=len(matrix),len(matrix[0])
        max_of_row=float("-inf")
        for r in range (row):
            row_min=min(matrix[r])
            max_of_row=max(row_min,max_of_row)
        for c in range(col):
            col_max=matrix[0][c]
            for r in range(row):
                col_max=max(col_max,matrix[r][c])
            if col_max==max_of_row:
                return [col_max]
        return []

            

        