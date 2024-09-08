class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        s=s.strip()
        if s and (s[0].isdigit() or s[0] in ['-','+']):
            for i in range(len(s)):
                if s[i].isdigit() or (i==0 and s[i] in ['-','+']):
                    ans += s[i]
                else:
                    break
            if ans in ['-','+']:
                ans = 0
            else:
                ans = int(ans)
            if (2**31) - 1 < ans:
                ans = (2**31) - 1
            elif ans < -2**31:
                ans = -2**31
        else:
            ans = 0
        return ans
