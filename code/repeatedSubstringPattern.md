# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/repeated-substring-pattern/submissions/)

给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200824133631810.png#pic_center)



# 2. 思路
自己写的就是简单的思路一，列出其他思路供参考。
#### 2.1 找到子串
子串最短长度为：集合的长度
子串最长长度为：原字符串的一半
在这个长度范围内查找：
   - 长度能被原字符串整除，得到子串个数
   - 子串*个数 == 原字符串，返回真
```python
    def repeatedSubstringPattern(self, s: str) -> bool:
        subs_min_len = len(set(s))
        subs_max_len = len(s) // 2

        for i in range(subs_min_len, subs_max_len + 1):
            if (len(s) / i) % 1 == 0 and s[:i] * int(len(s) / i) == s:
                return True
        return False
```
#### 2.2 双倍字符串
```python
   def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
```
双倍字符串，然后从**位置1**开始找
  - 如果s不是循环字串构成的，那么找到的位置一定是，len(s)，比如“1234  1234”
  - 如果由循环子串构成，一定可以找到非len(s)位置的s，“12**12 12**12”


# 3. 总结

~~总结这块要不去掉算了，可是删掉又感觉不太完整……~~ 







