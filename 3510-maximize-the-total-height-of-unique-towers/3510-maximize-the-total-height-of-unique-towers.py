class Solution:
  def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        # Count the frequency of each height
        height_count = Counter(maximumHeight)
        
        total_sum = 0
        assigned_heights = set()  # Set to track assigned heights
        
        # Sort unique heights in descending order
        unique_heights = sorted(height_count.keys(), reverse=True)

        for height in unique_heights:
            count = height_count[height]
            
            # Assign heights from this height down to avoid duplicates
            while count > 0:
                # Find the next unique height to assign
                while height in assigned_heights:
                    height -= 1  # Decrement until we find a unique height
                
                if height <= 0:  # If we go below zero, we can't assign anymore
                    return -1
                
                assigned_heights.add(height)  # Add the unique height to the set
                total_sum += height  # Add to the total sum
                count -= 1  # Use one of the counts of this height
        
        return total_sum


     

