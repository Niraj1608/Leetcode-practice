class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        list1 = zip(heights, names)

        ans= []
        for h, n in sorted(list1, reverse=True):
            ans.append(n)

        return ans