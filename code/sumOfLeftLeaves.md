
[原题地址](https://leetcode-cn.com/problems/sum-of-left-leaves/)

求左叶子之和。

简单题没啥好说的了。层次遍历就可以，标记一下左右就行。

```python
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 用层次遍历吧      
        # 1 表示左子树
        # 0 表示右子树
        if not root:
            return 0
        res = 0
        track = [[root, 0]]
        while track:
            cur, type_c = track.pop()
            if type_c == 1 and not cur.left and not cur.right:  # 叶子
                res += cur.val
            track.append([cur.left, 1]) if cur.left else None
            track.append([cur.right, 0]) if cur.right else None
        return res
```
