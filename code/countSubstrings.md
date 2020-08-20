# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/palindromic-substrings/)

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/2020081922392792.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)

# 2. 思路

首先是最简单的方案，暴力两层循环，形成所有子字符串，依次判断是否回文。
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        def _is(sub_s):
            return sub_s == sub_s[::-1]
        res = 0
        for i in range(len(s)):
            j = i + 1
            while j <= len(s):
                if _is(s[i:j]):
                    res += 1
                j += 1
            
        return res
```

然后想想怎么优化，单独的字符必定算回文，所以可以直接写成：
```python
        res = len(s)
```
然后再判断两个或者更多字符的回文，这分为两种情况：
- 偶数回文 ： abba ……
- 奇数回文 ： abcba ……
```python
    def countSubstrings(self, s: str) -> int:
        str_len = len(s)
        res = str_len

        def fuc(left, right): # 递归查找回文字符
            if left < 0 or right >= str_len:
                return 0
            if s[left] == s[right]:
                return fuc(left - 1, right + 1) + 1
            return 0

        for i in range(str_len - 1):
            for j in [i + 1, i + 2]: # j = i + 1 判断偶数回文,i+2判断奇数
                if j < str_len and s[i] == s[j]:
                    res += 1
                    res += fuc(i - 1, j + 1)

        return res
```
这样比第一种方式要快很多……


# 3. 总结

作者太懒了，没什么要总结的……


![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818163402886.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)







