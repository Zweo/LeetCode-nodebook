# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200826124334825.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)




# 2. 思路


在本题中，主要就是每个按键可以有不同的选择，在每个**节点**，也就是按下的数字位置有多个选择，这样就可以先选择一个，之后弹出这个元素，再选择下一个。
```python
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_str = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res = []
        path = []
        def comb(index):
            if index == len(digits):
                res.append(''.join(path))
                return
            for char in num_str[digits[index]]:
                path.append(char)
                comb(index+1)
                path.pop()
        comb(0)
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







