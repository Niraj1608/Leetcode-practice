class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def hrtomin(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        minutes=[hrtomin(tp) for tp in timePoints]
        
        # Step 2: Sort the minutes
        minutes.sort()

        min_diff=float('inf')
        for i in range(1,len(minutes)):
            min_diff=min(min_diff,minutes[i]-minutes[i-1])
        circular=1440-minutes[-1]+minutes[0]
        min_diff = min(min_diff, circular)
        
        return min_diff



    
        