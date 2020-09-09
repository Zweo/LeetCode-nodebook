# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/combination-sum/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。




# 2.思路
显然这是个回溯问题，首先把框架写出来。

```python3
    def fuc(self, tickets):
        path = [] # 记录路径
        res = [] # 多条路径，记录结果
        def backtrack(cur):
            if # 结束条件:
                # res.append(path[:])
            for 某节点 in 当前节点可以有的选择:
                # 去掉不合适选择
                path.append(某节点)  # 做选择
                if backtrack(某节点):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择
        backtrack(cur)
        return res
```



# 3.代码

```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        candidates.sort()

        def backtrack(track, cur_sum):
            if cur_sum == target: # 结束条件
                tmp = sorted(track)
                if tmp not in res: # 去重
                    res.append(tmp)
                return

            for i in candidates:
                if cur_sum + i > target:
                    break
                track.append(i)   # 做选择
                backtrack(track, cur_sum + i)  # 进入下一层决策树
                track.pop() # 取消选择

        backtrack(track, 0)

        return res

```
