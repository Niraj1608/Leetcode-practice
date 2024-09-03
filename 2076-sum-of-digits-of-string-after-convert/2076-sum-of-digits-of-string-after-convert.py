class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n=""
        for x in s:
            n+=str((ord(x)-ord('a'))+1)
        while k >0:
            temp=0
            for c in n:
                temp += int(c)
              
            n=str(temp)
            k-=1
        return int(n)



        