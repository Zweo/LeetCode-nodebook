class TreeNode:
    def __init__(self, x=0):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode):
        self.res = True

        def dfs(root: TreeNode):
            if not root or not self.res:  # res为False时，提前结束
                return 0
            l = dfs(root.left) + 1  # 左子树高度
            r = dfs(root.right) + 1  # 右子树高度
            if abs(l - r) > 1:  # 高度差大于1则令结果为False
                self.res = False
            return max(l, r)

        dfs(root)
        return self.res
