class Solution:
    def coinChange(self, coins: List[int], V: int) -> int:
        n = len(coins)
    
        dp = [[-1 for j in range(V+ 1)] for i in range(n)]
  
    
        def mini(arr,ind,t,dp):
            if ind==0:
                if t%arr[0]==0:
                    return t//arr[0]
                else:
                    return int(1e9)
                
            if dp[ind][t] != -1:
                return dp[ind][t]
            nottaken=0+mini(arr,ind-1,t,dp)
            taken=int(1e9)
            if arr[ind]<=t:
                taken=1+mini(arr,ind,t-arr[ind],dp)
            dp[ind][t]=min(nottaken,taken)
            return dp[ind][t]
        ans=mini(coins, n - 1, V, dp)

   
        if ans >= int(1e9):
            return -1
        return ans

