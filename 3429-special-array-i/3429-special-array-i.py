class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==1 :
            return True

        for i in range (n-1):
            if nums[i]%2==0:
                if nums[i+1]%2==0:
                    return False
            elif nums[i]%2!=0:
                if nums[i+1]%2!=0:
                    return False
        return True      
        