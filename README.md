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
        
  def inorderTraversal(self, root: TreeNode):
      '''迭代形式中序遍历'''
      res = []
      track = [root]
      while track:
          cur = track.pop()
          if isinstance(cur, TreeNode):
              track.extend([cur.right, cur.val, cur.left])
          elif isinstance(cur, int):
              res.append(cur.val)
      return res
 ```
#### 一些例题

###### 前序遍历
[leedcode109-有序链表转平衡二叉树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/sortedListToBST.md)

###### 后序遍历
[leedcode110-平衡二叉树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/isBalanced.md)

[leedcode111-二叉树最小深度](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/minDepth.md)

###### 层次遍历
[leedcode107-二叉树层次遍历](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/levelOrderBottom.md)

[leedcode226-翻转二叉树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/invertTree.md)



## 2.字符串问题

[leedcode647-回文子串](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/countSubstrings.md)

[leedcode459-重复子串](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/repeatedSubstringPattern.md)

[leedcode657-机器人能否返回原点](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/judgeCircle.md)



## 3.DFS
[leedcode529-扫雷游戏](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/updateBoard.md)

[leedcode841-钥匙和房间](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/canVisitAllRooms.md)


## 4.回溯问题

#### 掌握回溯算法基本框架
  ```python
 def func(self, nums):
     res = []
     def backtrack(nums, track, k):
         if 结束条件:
            return
         for i in range(k, len(nums)):
            backtrack(nums, track + [nums[i]], i + 1)  # 进入下一层决策树
        backtrack(nums, [], 0)
     return res
 ```

[leedcode17-电话号码的字母组合](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/letterCombinations.md)

[leedcode332-重新安排行程](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/findItinerary.md)

[leedcode51-N皇后](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/solveNQueens.md)

[leedcode39，40-组合总和](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/combinationSum.md)

[leedcode37-解数独](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/solveSudoku.md)

[leedcode47-全排列](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/permuteUnique.md)



## 5.图论

[leedcode685-冗余连接Ⅱ（困难）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/findRedundantDirectedConnection.md)








