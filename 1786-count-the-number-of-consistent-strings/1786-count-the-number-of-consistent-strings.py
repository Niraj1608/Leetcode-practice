class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allow = set(allowed)
        count = 0
        for w in words :
            res=True 
            for i in set(w):
                if i not in allow:
                    res=False
                    break
            if res==True:
                count+=1
        return count