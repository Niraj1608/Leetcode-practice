class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each number in nums1
        count = Counter(nums1)
        
        ans = []
        
        # Check each number in nums2
        for num in nums2:
            if count[num] > 0:
                ans.append(num)
                count[num] -= 1
        
        return ans