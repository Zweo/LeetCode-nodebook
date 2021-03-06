# LeetCode-nodebook
leedcode刷题记录

开始刷题了欸，记录一下解题思路，慢慢更新


## 1.二叉树问题

[掌握基本的遍历方式](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/遍历方式.py)
前序中序后序
层次遍历



#### 一些例题

###### 前序遍历
[有序链表转平衡二叉树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/sortedListToBST.md)

[二叉搜索树中的插入](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/insertIntoBST.md)



###### 中序遍历

[二叉搜索树转为累加树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/convertBST.md)

[二叉搜索树的最小绝对差](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/getMinimumDifference.md)



###### 后序遍历
[平衡二叉树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/isBalanced.md)

[二叉树最小深度](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/minDepth.md)




###### 层次遍历

[二叉树层次遍历](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/levelOrderBottom.md)

[翻转二叉树](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/invertTree.md)

[左叶子之和](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/sumOfLeftLeaves.md)

[填充每个节点下一个右侧节点](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/connect.md)





## 2.字符串问题

[回文子串](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/countSubstrings.md)

[重复子串](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/repeatedSubstringPattern.md)

[机器人能否返回原点](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/judgeCircle.md)



## 3.DFS
[扫雷游戏](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/updateBoard.md)

[钥匙和房间](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/canVisitAllRooms.md)

[子集](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/subsets.md)




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

[电话号码的字母组合](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/letterCombinations.md)

[重新安排行程](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/findItinerary.md)

[N皇后](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/solveNQueens.md)

[组合总和](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/combinationSum.md)

[解数独](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/solveSudoku.md)

[全排列](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/permuteUnique.md)

[单词拆分II（困难）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/wordBreak.md)



## 5.图论

[冗余连接Ⅱ（困难）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/findRedundantDirectedConnection.md)



## 6.链表

[回文链表（简单）](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/isPalindrome.md)


## 7.其他
[有多少小于当前数字的数字](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/smallerNumbersThanCurrent.md)

[根据有多少位数1排序](https://github.com/Zweo/LeetCode-nodebook/blob/master/code/sortByBits.py)



