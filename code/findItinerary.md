# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

> 1. 如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前 
> 2. 所有的机场都用三个大写字母表示（机场代码）。
> 3. 假定所有机票至少存在一种合理的行程。

示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200827141700573.png#pic_center)



# 2.思路
显然这是个回溯问题，首先把框架写出来。

```python3
    def findItinerary(self, tickets):
        path = [] # 记录路径
        # res = [] # 多条路径，记录结果
        def backtrack(cur):

            if # 结束条件:
                # res.append(path[:])
                return True

            for 某节点 in 当前节点可以有的选择:
                # 去掉不合适选择
                path.append(某节点)  # 做选择
                if backtrack(某节点):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择

            return False
        backtrack(cur)
        return path
```

在本题中，就是从'JKF'开始，然后选择'JKF'可以到达的机场：

- **结束条件：遍历完所有路径，path的长度 应当为字符串二维数组长度 + 1**
- **循环结构：每次取出某节点后，将这个节点从备用选择中删除，防止出现循环路径**

用字典把对应的机场位置存储起来，变成如图所示的状态，然后就好求解了：
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020082714180653.png#pic_center)



# 3.代码

```python3
class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        ticket_dict = defaultdict(list)
        for item in tickets:
            ticket_dict[item[0]].append(item[1])

        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:  # 结束条件
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)  # 删除当前节点
                path.append(cur_to)  # 做选择
                if backtrack(cur_to):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择
                ticket_dict[cur_from].append(cur_to)  # 恢复当前节点
            return False

        backtrack('JFK')
        return path
```
