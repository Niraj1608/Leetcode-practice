class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newcolor: int) -> List[List[int]]:
        def dfs(row,col,ans,image,newcolor,initalcolor,delrow,delcol):
            ans[row][col] = newcolor
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if nrow>=0 and ncol>=0 and nrow <len(image) and ncol < len(image[0]) and image[nrow][ncol]==initalcolor and ans[nrow][ncol]!=newcolor:
	                dfs(nrow,ncol,ans,image,newcolor,initalcolor,delrow,delcol)
            
        
        initalcolor = image[sr][sc]
        ans = image[::]
        delrow = [-1,0,+1,0]
        delcol = [0,+1,0,-1]

        dfs(sr,sc,ans,image,newcolor,initalcolor,delrow,delcol)
        return ans