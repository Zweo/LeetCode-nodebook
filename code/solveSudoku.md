# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/sudoku-solver/)


一个数独的解法需遵循如下规则：

	数字 1-9 在每一行只能出现一次。
	数字 1-9 在每一列只能出现一次。
	数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
	空白格用 '.' 表示。
| 输入 | 输出 |
|--|--|
| ![在这里插入图片描述](https://img-blog.csdnimg.cn/202009151730437.png#pic_center) | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200915173049760.png#pic_center) |



# 2.思路

解数独本质上就是填入一个数字，判断是否满足条件，不行就换下一个数字。
这就很像回溯问题。

先搬出回溯算法框架：
```python
def func(self, nums):
    def backtrack():
        if 结束条件:
           return
        for i in 可选项:
            做选择
            进入下一层决策树
            撤销选择
    backtrack()
```

**结束条件：**
   
   - row = 9 时结束，因为所有行都填完了。
    - col = 9 时单行结束，单行9列，进入下一行。


**可选项：**    用[1-9]集合 减去[行，列，区域] 已经出现的数字集合，就是可以选择的数字


**决策：**    

   - 当前位置改为选择的num
    - 进入下一层
    - 当前位置改回'.'




# 3.代码
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def candidate(i, j):
            old = set(board[i])  # 横向
            [old.add(board[t][j]) for t in range(9)]  # 纵向
            m_a, n_a = i // 3, j // 3  #区域
            for m in range(3):
                for n in range(3):
                    old.add(board[m_a * 3 + m][n_a * 3 + n])
            return set('123456789') - old

        def backtrack(row, col):
            if row == 9:  # 结束条件
                return True
            if col == 9:  # 单行结束条件
                return backtrack(row + 1, 0)
            if board[row][col] != '.':
                return backtrack(row, col + 1)  #　进入下一层决策树
            for num in candidate(row, col):
                board[row][col] = num  # 做选择
                if backtrack(row, col + 1):  #　进入下一层决策树
                    return True
                board[row][col] = '.'  # 撤回选择
            return False

        backtrack(0, 0)
```

https://github.com/Zweo/LeetCode-nodebook
