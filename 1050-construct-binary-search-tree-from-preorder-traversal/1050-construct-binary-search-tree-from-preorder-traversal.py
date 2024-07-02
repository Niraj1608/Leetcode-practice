# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #base case
        if not preorder:
            return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        #create root
        root = TreeNode(preorder[0])
        #iterate array to find left end right
        i=1
        for j in range(1,len(preorder)):
            if preorder[j]<preorder[0]:
                i+=1
        root.left=self.bstFromPreorder(preorder[1:i])
        root.right=self.bstFromPreorder(preorder[i:])
        return root


        