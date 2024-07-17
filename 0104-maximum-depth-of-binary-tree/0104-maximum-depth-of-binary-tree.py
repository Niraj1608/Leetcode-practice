# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #use level order traversal
        if root is None:
            return 0
        q=Queue()
        level=0
        q.put(root)
        while not q.empty():
            #get the no. of nodes
            #at the current level
            size=q.qsize()
            for i in range(size):
                front=q.get()
                if front.left is not None:
                    q.put(front.left)
                if front.right is not None:
                    q.put(front.right)
            level+=1

        return level
            



        