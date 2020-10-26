### 解题思路

https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/

先数一数每个数有多少个。存在字典中
字典按从小到大排列。

按照 Vi = Vi-1,就可以得到答案。
由于i-1已经被修改，所以用个临时变量存储Vi-1就好了

最小的值的Vi-1为0,所以tmp初始化为0

### 代码

```python3
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        res_dict = {}
        for i in range(len(nums)):
            if nums[i] in res_dict:
                res_dict[nums[i]] += 1
            else:
                res_dict[nums[i]] = 1
        tmp = 0
        for key in sorted(res_dict):
            tmp, res_dict[key] = res_dict[key] + tmp, tmp

        return [res_dict[num] for num in nums]
```
