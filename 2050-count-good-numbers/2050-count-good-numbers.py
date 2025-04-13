class Solution:

    
    def countGoodNumbers(self, n: int) -> int:

        mod=10**9+7
        def pow(x,n):
            if n==0:return 1
            if n==1:return x
            if n % 2==0:
                ans=pow(x,n/2)
                return (ans*ans)%mod
            else:
                ans=pow(x,(n-1)/2)
                return (x*ans*ans)%mod
        odd = n // 2
        even = n-odd
        res = ((pow(4,odd)%mod*pow(5,even)%mod)%mod)
        return res

        


