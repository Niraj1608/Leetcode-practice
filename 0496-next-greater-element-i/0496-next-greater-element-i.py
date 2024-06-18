class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hash map of nums2 for quick O(n) look up
        h = {}
        stack = []
        for i in range(0, len(nums2)):
            if len(stack) == 0:
                stack.append(nums2[i])
                continue
            if nums2[i] > stack[-1]:
                # process the stack in reverse
                n = stack.pop()
                while n < nums2[i]:
                    h[n] = nums2[i]
                    if len(stack) > 0 and stack[-1] < nums2[i]:
                        n = stack.pop()
                    else:
                        break
                # add current value to new stack
                stack.append(nums2[i])
            else: # equal to or less
                stack.append(nums2[i])
        ans = []
        for i in nums1:
            if i in h:
                ans.append(h[i])
            else:
                ans.append(-1)
        return ans