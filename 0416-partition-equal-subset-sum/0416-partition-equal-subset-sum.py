class Solution:

    def canPartition(self, arr: List[int]) -> bool:
        total=sum(arr)
        n=len(arr)
        if total%2==1:
            return False
      
        k=total//2
        dp = [[False for j in range(k+1)] for i in range (n)]
        for i in range(n):
            dp[i][0]=True
        if arr[0]<=k:
            dp[0][arr[0]]=True
        for ind in range(1,n):
            for target in range(1,k+1):
                notTaken = dp[ind - 1][target]
                    
                # If the current element is taken, subtract its value from the target and check the previous row.
                taken = False
                if arr[ind] <= target:
                    taken = dp[ind - 1][target - arr[ind]]
                    
                    # Update the DP table with the result of taking or not taking the current element.
                dp[ind][target] = notTaken or taken
        
        # The final result is stored in the bottom-right cell of the DP table.
        return dp[n - 1][k]

         