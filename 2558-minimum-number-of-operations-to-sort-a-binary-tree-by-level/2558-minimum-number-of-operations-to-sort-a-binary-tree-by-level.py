# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def countops(nums):
            swaps=0
            sorted_num= sorted(nums)
            index_map={n:i for i,n in enumerate(nums)}
            for i in range(len(nums)):
                if nums[i] != sorted_num[i]:
                    swaps += 1
                    j=index_map[sorted_num[i]]
                    nums[i],nums[j]=nums[j],nums[i]
                    index_map[nums[j]]=j
            return swaps
        q=deque([root])
        ans=0
        while q:
            level=[]
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans+=countops(level)
        return ans

