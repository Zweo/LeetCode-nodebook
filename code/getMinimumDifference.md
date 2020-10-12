### 解题思路

[原题地址](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)

二叉搜索树，中序遍历是从小到大的。
然后用后一个数减去前一个数
·用last记录前一个数
·用res记录差值的最小值。

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = float('inf')
        last = -1

        # 中序遍历，从小到大
        def dfs(node):
            nonlocal last,res
            if not node:
                return
            dfs(node.left)
            if last != -1:
                res = min(node.val - last, res)
            last = node.val
            dfs(node.right)


        dfs(root)

        return res
```
