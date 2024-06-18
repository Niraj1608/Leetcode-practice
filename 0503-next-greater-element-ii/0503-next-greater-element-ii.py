class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        for i in range(len(nums)-1,-1,-1):
            st.append(nums[i])
        
        nge = [-1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            while st and st[-1] <= nums[i]:
                st.pop()
            if st:
                nge[i] = st[-1]
            else:
                nge[i] = -1
            st.append(nums[i])
        
        return nge
        