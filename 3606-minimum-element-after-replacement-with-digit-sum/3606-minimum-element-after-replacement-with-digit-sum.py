class Solution:
    def digit_sum(self, num: int) -> int:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        return sum_digits

    def minElement(self, nums: list[int]) -> int:
        # Use self.digit_sum() since digit_sum is now a method of the class
        nums = [self.digit_sum(num) for num in nums]
        # Return the minimum element from the list
        return min(nums)