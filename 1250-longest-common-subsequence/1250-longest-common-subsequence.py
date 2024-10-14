class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n = len(s1)
        m = len(s2)

       
        dp = [[-1 for j in range(m)] for i in range(n)]

        def lcs(s1, s2, ind1, ind2, dp):
            if ind1 < 0 or ind2 < 0:
                return 0
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            if s1[ind1] == s2[ind2]:
                dp[ind1][ind2] = 1 + lcs(s1, s2, ind1 - 1, ind2 - 1, dp)
            else:
                dp[ind1][ind2] = max(lcs(s1, s2, ind1, ind2 - 1, dp), 
                                     lcs(s1, s2, ind1 - 1, ind2, dp))
            return dp[ind1][ind2]

        return lcs(s1, s2, n - 1, m - 1, dp)
