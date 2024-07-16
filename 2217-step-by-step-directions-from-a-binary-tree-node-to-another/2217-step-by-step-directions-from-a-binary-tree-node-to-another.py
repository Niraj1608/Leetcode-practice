# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(curr,dest,path):
            if not curr:
                return 
            
            if curr.val==dest:
                return True

            if findPath(curr.left,dest,path):
                path.append('L')
                return True
            
            if findPath(curr.right,dest,path):
                path.append('R')
                return True

        s,d = [],[]
        findPath(root,startValue,s)
        findPath(root,destValue,d)

        while s and d and s[-1]==d[-1]:
            s.pop()
            d.pop()

        return 'U'*len(s)+''.join(d[::-1])


            
        