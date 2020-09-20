### 解题思路
[原题地址](https://leetcode-cn.com/problems/subsets/)

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

	说明：解集不能包含重复的子集。
	
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200920141644293.png#pic_center)


画出决策树

![image.png](https://img-blog.csdnimg.cn/img_convert/24757dc44356c3851527a9a1811fa854.png)

在每一层中选择当前数字，不选择当前数字，分别进入下一层。

### 代码

```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(track, index):
            if index == len(nums):
                res.append(track)
                return
            backtrack(track + [nums[index]], index + 1)
            backtrack(track + [], index + 1)
        backtrack([], 0)
        return res
        
```
