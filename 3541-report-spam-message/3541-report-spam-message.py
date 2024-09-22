class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned=set(bannedWords)
        count=0
        maxcount=2
        for i in message:
            if i in banned:
                count+=1
            if count >= maxcount:
                return True
        return False


        
        