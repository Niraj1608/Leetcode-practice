class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda type: -type[1])
        for box, unit in boxTypes:
            pack = min(box, truckSize)
            truckSize -= pack
            ans += pack * unit
            if truckSize == 0:
                break
        return ans