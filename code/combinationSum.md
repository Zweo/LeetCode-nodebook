# 1. 问题

[Leetcode原题地址-组合1](https://leetcode-cn.com/problems/combination-sum/)

[Leetcode原题地址-组合2](https://leetcode-cn.com/problems/combination-sum-ii/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

第一个问题是可以重复选取。
第二个问题是每个元素只能选取一次。

# 2.思路
显然这是个回溯问题，首先把框架写出来。

```python3
    def fuc(self, nums):
        res = [] 
        def backtrack(nums, track, index):
            if # 结束条件:
                # res.append(track)
            for cur in nums:
                backtrack(nums, track + [cur], 0)
        backtrack(nums, [], 0)
        return res
```

# 3.代码
问题一解法
```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(nums, track, k):
            if sum(track) > target:
                return
            elif sum(track) == target:  # 结束条件
                tmp = sorted(track)
                if tmp not in res:  # 去重
                    res.append(tmp)
                return

             for i in range(k, len(nums)):
                backtrack(nums, track + [nums[i]], 0)  # 进入下一层决策树
                
        backtrack(candidates, [], 0)
        
        return res

```
问题二解法
```python
    def combinationSum2(self, candidates, target: int):
        res = []

        def backtrack(nums, track, k):
            if sum(track) > target:
                return
            elif sum(track) == target:  # 结束条件
                tmp = sorted(track)
                if tmp not in res:  # 去重
                    res.append(tmp)
                return

            for i in range(k, len(nums)):
                backtrack(nums, track + [nums[i]], i + 1)  # 进入下一层决策树

        backtrack(candidates, [], 0)

        return res
```

两个结合起来看，重复选取就是递归下一层时，一个从0开始，一个从下一位置开始。
