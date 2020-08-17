## 1.平衡二叉树问题
[Leetcode原题地址](https://leetcode-cn.com/problems/balanced-binary-tree/)

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

![平衡](https://img-blog.csdnimg.cn/20200817185230928.png)   ![不平衡](https://img-blog.csdnimg.cn/20200817185254558.png)

例如上图，左边的是平衡的，右边的不是。 

## 2.解题思路
首先掌握二叉树遍历的基础，分别有如下三种形式，然后往里面套就行了。 

```python
def visitTree(root: TreeNode):
    if not root:
        return
    # 前序遍历
    visitTree(root.left)
    # 中序遍历
    visitTree(root.right)
    # 后序遍历
```

比较清晰的一个思路是，计算左子树深度，计算右子树深度，判断高度差是否大于1，那么很自然就可以得到如下代码。

```python
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
```

## 3.总结
      总的来说是一道简单题，不过掌握了解题套路之后就好做了。给大家推荐一个大佬的网站，总结了一些刷题方法，二叉树相关一切问题本质上还是前序遍历，中序遍历，后序遍历。这个思路也是从这里学到的：https://labuladong.gitbook.io/

     em，最近开始写写公众号了，主要是写一些人生感悟什么的，还会分享一些书籍，之后也会更新一些技术文章吧，虽然技术也不咋地，一起学习进步吧！
     
    ![1](https://github.com/Zweo/LeetCode-nodebook/blob/master/resources/gongzhonghao.jpg)
