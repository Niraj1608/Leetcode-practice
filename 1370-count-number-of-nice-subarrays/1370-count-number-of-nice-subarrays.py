class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
        l = m = r = 0
        odd = 0
        count = 0
        while r < len(arr):
            if arr[r] % 2 == 1:
                odd = odd + 1

            while odd > k:
                if arr[l] % 2 == 1:
                    odd = odd - 1
                l = l + 1
                m = l
                
            if odd == k:
                while arr[m] % 2 != 1:
                    m = m + 1
                count = count + m - l + 1
            r = r + 1

        return count