class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row,col=len(rowSum),len(colSum)
        res=[[0]* col for _ in range(row)]
        #pehli row ma badho j sum nakhi dye row no
        for r in range (row):
            res[r][0]+=rowSum[r]

        for c in range (col):
            cur_col_sum=0
            for r in range (row):
                cur_col_sum+=res[r][c]
            r=0
            while cur_col_sum>colSum[c]:
                diff=cur_col_sum-colSum[c]
                maxshift=min(diff,res[r][c])
                res[r][c]-=maxshift
                res[r][c+1]+=maxshift
                cur_col_sum-=maxshift
                r+=1
        return res






        