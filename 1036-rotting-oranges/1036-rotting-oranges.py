class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        m,n = len(grid),len(grid[0])
        #find rotten orange
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))

        #Find the max depth of spread to all connected oranges
        directions = [(0,-1),(-1,0),(1,0),(0,1)]
        max_depth = 0 #max minutes
        while queue:
            x,y, minute = queue.pop(0)
            for d_x, d_y in directions:
                n_x,n_y = x+d_x,y+d_y
                if -1<n_x<m and -1<n_y<n and grid[n_x][n_y]==1:
                    grid[n_x][n_y]=2
                    queue.append((n_x,n_y,minute+1))
                    max_depth= max(max_depth,minute+1)

        #Check if it is impossible
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return max_depth
