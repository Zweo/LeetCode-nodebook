# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)

给定一个二叉树，找出其最小深度。

> 最小深度:从**根节点**到**最近叶子节点**的**最短路径**上的**节点数量**


示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200821132839618.png#pic_center)


# 2. 思路
```python
def traverse(root: TreeNode):
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历
```

深度优先搜索，到达根节点返回，每次深度+1，取所有路径中最短。
```python
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:  # 空
            return 0
        if not root.left and not root.right:  # 叶节点
            return 1
        l = self.minDepth(root.left) + 1 if root.left else float('inf')
        r = self.minDepth(root.right) + 1 if root.right else float('inf')
        return min(l, r)
```

还可以有个优化的思路就是，存储当前最小深度，当递归深度大于等于这个值时就返回，从而剪枝。


# 3. 总结

又是二叉树~总之本质上问题还是那几个，前序中序后序遍历什么的，总之往这里套就完了……








