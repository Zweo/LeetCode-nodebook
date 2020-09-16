
### 问题：翻转二叉树

[原题地址](https://leetcode-cn.com/problems/invert-binary-tree/)

层次遍历，左右子树交换。

### 代码

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        track = [root]
        res = root
        while track:
            cur = track.pop()
            track.append(cur.left) if cur.left else None
            track.append(cur.right) if cur.right else None
            cur.left, cur.right = cur.right, cur.left
        return res
```
