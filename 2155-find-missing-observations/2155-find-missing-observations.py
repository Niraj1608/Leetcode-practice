class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        total=mean*(n+m)
        missing=total-sum(rolls)
        if missing>6*n or missing<n:
            return []
        res=[]
        while n:
            curr=min(6,missing-n+1)
            res.append(curr)
            missing-=curr
            n-=1
        return res
        