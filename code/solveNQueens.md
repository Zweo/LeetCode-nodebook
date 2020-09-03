# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/n-queens/submissions/)

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200903134304157.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)
# 2. 思路
对于n*n的棋盘，
首先在第**1**行第**1**列放置一个皇后Q
然后是第**2**行第**？**列，满足上下斜向不冲突条件。
……

最后第**n**行放置Q， 保存此时结果.

……
在第**1**行第**2**列放置一个皇后Q
 在第**1**行第**n**列放置一个皇后Q


```python
class Solution:
    def solveNQueens(self, n: int):
        res = []  # 记录所有解法
        tmp = '.' * n
        track = [tmp] * n  # 路径：记录在 track 中
        
        def is_valid(i, j):
            for t in range(i):  # 纵向
                if track[t][j] == 'Q':
                    return False
            t, k = i - 1, j - 1
            while t >= 0 and k >= 0:  # 左上
                if track[t][k] == 'Q':
                    return False
                t -= 1
                k -= 1
            t, k = i - 1, j + 1
            while t >= 0 and k < n:  # 右上
                if track[t][k] == 'Q':
                    return False
                t -= 1
                k += 1
            return 'Q' not in track[i][:j]  # 横向

        def backtrack(row):
            if row == n:
                res.append(track[:])
                return
            for col in range(n):
                if not is_valid(row, col):  # 排除不合法的选择
                    continue
                track[row] = tmp[:col] + 'Q' + tmp[col + 1:]  # 做选择
                backtrack(row + 1)  # 进入下一层决策树
                track[row] = tmp  # 取消选择

        backtrack(0)

        return res
```
# 3. 总结

- 回溯问题，掌握框架。
```python
def permute(nums):
    res = []      # 结果：保存结果路径
    track = []    # 路径：记录在 track 中
    def backtrack(nums, track):
        if  结束条件：
            res.append(track[:])
            return
        for i in 可选择的选项:
            track.append(i)            # 做选择
            backtrack(nums[1:], track)  # 进入下一层决策树
            track.pop()    # 取消选择
    backtrack(nums, track)
    return res
```







