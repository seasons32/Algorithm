class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution(object):
    def inorderTraversal(self, root):
        arr = list()
        if root :
            if root.left :
                arr.extend(Solution().inorderTraversal(root.left))

            if root :
                arr.append(root.val)

            if root.right :
                arr.extend(Solution().inorderTraversal(root.right))

        return arr


        
# [1,null,2,3]
root = TreeNode()
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
sol = Solution()
print(sol.inorderTraversal(root))
