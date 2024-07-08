class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum=0
        mpp=defaultdict(int)
        count=0
        mpp[0]=1
        n=len(nums)
        for i in range (n):
            presum+=nums[i]
            remove=presum-goal
            count+=mpp[remove]
            mpp[presum]+=1
        return count
