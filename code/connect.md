### 问题

[Leetcode原题](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。


### 代码

```python
class Solution:
    def connect(self, root):
        if not root:
            return root

        layer = 0
        queue = [[root, layer]]

        while queue:
            node, cur_lay = queue.pop(0)
            if not queue or queue[0][1] != cur_lay:
                node.next = None
            else:
                node.next = queue[0][0]
            queue.append([node.left, cur_lay + 1]) if node.left else None
            queue.append([node.right, cur_lay + 1]) if node.right else None

        return root
```
