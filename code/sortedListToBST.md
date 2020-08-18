# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/)

给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

> （平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1）

示例：
给定的有序链表： [-10, -3, 0, 5, 9],
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818150004787.png#pic_center)

昨天正好做了什么是平衡二叉树哈·

# 2. 思路
##### 2.1 思路一  

分析一下

首先，要平衡，上面长度为5的链表，**先存中间的值，比它小的放左边，比它大的放右边**。

但是长度为10或更多肯定不能直接这么放，那一点都不平衡。

由上述可推论，短序列可以按照这种方式，长的就会出现问题，那么就可以自然地考虑到，**二分法**将长的截成短的，再通过这种方式存放。

不过由于输入的结构是**链表**，只能顺序读取。先试着转换成数组列表，再按照这种思路执行吧，只是这样要花费些时间。

```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        input_list = []
        while head:
            input_list.append(head.val)
            head = head.next
        length = len(input_list)   # 转换成数组

        def build_tree(input_list, left, right): # 二分存储为树
            if left >= right:
                return None
            mid = (left + right) // 2
            res = TreeNode(input_list[mid])
            res.left = build_tree(input_list, left, mid)
            res.right = build_tree(input_list, mid + 1, right)
            return res

        res = build_tree(input_list, 0, length)
        return res
```

# 3. 总结

本质上还是个树的遍历问题，build_tree中使用的前序遍历，看到有其他的解法不转为数组，直接使用链表，可以靠中序遍历解决。嗯，太复杂了，还是搞简单点。


                                     “每天退步一点点，每天年轻一点点……”
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818163402886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)







