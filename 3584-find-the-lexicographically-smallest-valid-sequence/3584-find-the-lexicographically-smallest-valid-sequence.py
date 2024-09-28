class Solution:
    def validSequence(self, s1: str, s2: str) -> List[int]:
        n=len(s1)
        m=len(s2)
        # For Storing the last_index of each char in S2
        last_index=[0]*m
        j=m-1
        i=n-1
   
        while i>=0 and j>=0:
            if s1[i]==s2[j]:
                last_index[j]=i
                j-=1
            i-=1
    
        Took=0
        index=[]
        j=0
        for i in range(n):
           
            if j==m:
                break
        
            if s1[i]==s2[j]:
                index.append(i)
                j+=1
            else:
             
                if Took:
                    continue
            
                if j==m-1:
                    index.append(i)
                    break
      
                if last_index[j+1]>i:
                    index.append(i)
           
                    Took=1
                    j+=1
        return index if len(index)==m else []