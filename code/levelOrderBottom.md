# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200906160928536.png#pic_center)

# 2. 思路
层次遍历，用列表存储每一层的数值，最后反序。
主要就是掌握二叉树的层次遍历。


# 3. 代码
```python
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        res = [[]]
        track = [(0, root)]
        layer = 1
        while track:
            c, cur = track.pop(0)
            if c >= len(res):
                res.append([])
                layer += 1
            res[c].append(cur.val)
            track.append((layer, cur.left)) if cur.left else None
            track.append((layer, cur.right)) if cur.right else None
        return res[::-1]
```



