class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
		#total = sum([i*j for i,j in boxTypes]) 
		#if total <= truckSize: 
		#	return total
		#else:
        boxTypes.sort(key=lambda x:x[1], reverse=True) # sort the boxType list by capacity instead of quantity O(NlogN)
        boxes=0
        max_units = 0
        i=0
		# we keep going with our loop till we cannot fit any more boxes or till we have fit all the boxes. 
		# worst case will be we look through the entire boxTypes list and fit it all into the truck causing N iterations and giving O(N) runtime.
		# We can potentially shortcircuit it aswell by testing if all the boxTypes can be fit or not. 
		# If not, then we execute the code below. That's a decent optimization, however. I'll keep it simple for now.
        while boxes <= truckSize and i < len(boxTypes):
            remaining_cap = (truckSize - boxes)
            if remaining_cap > boxTypes[i][0]:
                max_units += (boxTypes[i][0]*boxTypes[i][1])
                boxes += boxTypes[i][0]
            else:
                max_units += (remaining_cap*boxTypes[i][1])
                boxes += remaining_cap
            i+=1
        return max_units
