class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        n=len(tri)
 
        dp=[[-1 for j in range(n)]for i in range(n)]
        def f (i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i==n-1:
                return tri[i][j]

            down=tri[i][j]+f(i+1,j)
            dia=tri[i][j]+f(i+1,j+1)
            dp[i][j]=min(down,dia)
            return dp[i][j]
         
        return f(0,0)
