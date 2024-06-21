class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        window,maxwin=0,0
        l=0
        sat=0
        for r in range(len(customers)):
            if grumpy[r]:
                window+=customers[r]
            else:
                sat+=customers[r]
            if r-l+1>minutes:
                if grumpy[l]:
                    window-=customers[l]
                l+=1
            maxwin=max(window,maxwin)
        return sat+maxwin

        
        