### 问题
[原题地址](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/)

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

	二叉搜索树：左节点值 < 根节点值 < 右节点值
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020092116243314.png#pic_center)

用先右后左的中序遍历，依次累加就可以了。

啧啧啧

### 代码

```python3
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        track = []

        def dfs(node):  # 逆中序遍历
            if not node:
                return
            dfs(node.right)  # 右
            track.append(node)
            if len(track) > 1:
                track[-1].val += track[-2].val
            dfs(node.left)  # 左

        dfs(root)

        return root
```
