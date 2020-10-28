### 解题思路

[701.二叉树种插入操作](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/)

迭代方式来一波吧~
根据二叉搜索树的性质，若大于当前节点，放进右边，否则左边，直至找到一个空节点。

### 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        track = [root]

        while track:
            cur = track[-1]

            if not cur:
                if val > track[-2].val:
                    track[-2].right = TreeNode(val)
                else:
                    track[-2].left = TreeNode(val)
                break

            track.append(cur.left if val < cur.val else cur.right)
        return root
```
