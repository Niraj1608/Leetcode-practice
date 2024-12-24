# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global ans
        ans=0
        
     
        def height(root):
            if root is None:
                return 0
            global ans
        
            lh=height(root.left)
            rh=height(root.right)
            ans=max(ans,rh+lh)
            return max(lh,rh)+1
        height(root)
        return ans
              




        
        