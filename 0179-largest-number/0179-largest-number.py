from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(l) for l in nums]
                
        def comp(num1, num2):
            a = int(num1 + num2)
            b = int(num2 + num1)
            if a > b:
                return -1
            if b > a:
                return 1
            return 0
        
        nums = sorted(nums, key=cmp_to_key(comp))
        res = "".join(nums)
        while len(res) > 1 and res[0] == "0":
            res = res[1:]
        return res