class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sumk=sum(chalk)
        mod=k%sumk
        n=len(chalk)
        for i in range(n):
            if chalk[i]>mod:
                
                return i
            mod-=chalk[i]
        return mod


      

