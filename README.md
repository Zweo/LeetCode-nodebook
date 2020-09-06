# LeetCode-nodebook
leedcode刷题记录

开始刷题了欸，记录一下解题思路，慢慢更新


## 1.二叉树问题


#### 掌握基本的遍历方式
  ```python
  def traverse(root: TreeNode):
    if not root:
        return
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历
    
 def path(root: TreeNode):
    '''层次遍历'''
    queue = [root]
    while queue:
        cur = queue.pop()
        queue.append(root.left) if root.left else None
        queue.append(root.right) if root.right else None
        print(cur.val)
 ```
#### 一些例题

###### 前序遍历
[leedcode109-有序链表转平衡二叉树（前序遍历）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/sortedListToBST.md)

###### 后序遍历
[leedcode110-平衡二叉树（后序遍历）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/isBalanced.md)

[leedcode111-二叉树最小深度（后序遍历）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/minDepth.md)

###### 层次遍历
[leedcode107-二叉树层次遍历（层次遍历）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/levelOrderBottom.md)




## 2.字符串问题

[leedcode647-回文子串](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/countSubstrings.md)

[leedcode459-重复子串](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/repeatedSubstringPattern.md)

[leedcode657-机器人能否返回原点](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/judgeCircle.md)



## 3.DFS
[leedcode529-扫雷游戏](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/updateBoard.md)

[leedcode841-钥匙和房间](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/canVisitAllRooms.md)


## 4.回溯问题

[leedcode17-电话号码的字母组合](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/letterCombinations.md)

[leedcode332-重新安排行程](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/findItinerary.md)

[leedcode51-N皇后](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/solveNQueens.md)








