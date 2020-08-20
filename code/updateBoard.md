# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/minesweeper/)

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

1. 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
2. 如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
3. 如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
4. 如果在此次点击中，若无更多方块可被揭露，则返回面板。


示例：
|字符串  |图解  |
|--|--|
|![在这里插入图片描述](https://img-blog.csdnimg.cn/20200820171022361.png#pic_center)  | ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200820171031953.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center) |


# 2. 思路
- 如果点击位置为**M**：修改为**X**，返回
- 如果点击位置为**E**：递归查询， 往上下左右四个斜角，共8个方向开始搜索。
   1. 如果含有**M**,，修改当前位置的值，并且不再递归查询
   2. 如果没有**M**，当前位置改为**B**，并且递归查询剩余其他**E**位置（不需要查询非**E**位置）

按照这个思路，就能比较清晰地写出来了……

```python
class Solution:
    def updateBoard(self, board, click):
        m, n = len(board), len(board[0])
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        else:
            m_num = 0
            neibor = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1),
                      (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            for k1, k2 in neibor:
                if 0 <= k1 < m and 0 <= k2 < n if board[k1][k2] == 'M':
                    m_num += 1

            if m_num == 0:
                board[i][j] = 'B'
                for k1, k2 in neibor:
                    if 0 <= k1 < m and 0 <= k2 < n and board[k1][k2] == 'E':
                        self.updateBoard(board, [k1, k2])
            else:
                board[i][j] = str(m_num)

        return board
```



# 3. 总结

作者太懒了，没什么要总结的……
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818163402886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)







