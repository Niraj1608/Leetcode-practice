class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
       #Adding more details to help on intuition, you have numBottles, you take out one full bottle aside, for each step,
       # you drink that bottle, and you take (numExchange-1) from your empty bottles,
       # and exchange them to one full bottle and put it back. So the extra bottles number is: 
       #(numBottles-1)//(numExchange-1)
        return numBottles + (numBottles-1)//(numExchange-1)
            

        
        
        