

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def isPossible(maxTime, mountainHeight, workerTimes):
            totalHeight = 0
            for time in workerTimes:
                h = 0
                current_time = 0
                while current_time + (h + 1) * time <= maxTime:
                    h += 1
                    current_time += h * time
                totalHeight += h
                
                if totalHeight >= mountainHeight:
                    return True
            return totalHeight >= mountainHeight

        # Binary search for the minimum time
        low, high = 0, 1
        while not isPossible(high, mountainHeight, workerTimes):
            high *= 2
        
        while low < high:
            mid = (low + high) // 2
            if isPossible(mid, mountainHeight, workerTimes):
                high = mid
            else:
                low = mid + 1
        
        return low
