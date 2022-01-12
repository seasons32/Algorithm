class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if p.val == q.val:
            return sol.isSameTree(p.left, q.left) and sol.isSameTree(p.right, q.right)
        else:
            return False
        

p = TreeNode()
p.right = TreeNode(2)
p.right.left = TreeNode(3)

q = TreeNode()
q.right = TreeNode(2)
q.right.left = TreeNode(3)

sol = Solution()
print(sol.isSameTree(p, q))
