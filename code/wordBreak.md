### 解题思路

[原题地址](https://leetcode-cn.com/problems/word-break-ii/)

回溯算法

结束条件：访问完所有字符
判断条件：判断前n个字符是否在字典中

因为有个aaaaaaaaaaaaaaaabaaaaaaaaaa 
和aa aaaa aaaa的例子，
前面加上一个判断，s的集合若大于wordDict的集合，就直接返回空

### 代码

```python3
class Solution:
    def wordBreak(self, s: str, wordDict):
        res = []
        if (set(s) > set(''.join(wordDict))):
            return []
        def backtrack(index, track):
            if (index >= len(s)):
                res.append(' '.join(track))
                return
            for j in range(index + 1, len(s) + 1):
                if (s[index:j] in wordDict):
                    backtrack(j, track + [s[index:j]])

        backtrack(0, [])

        return res
```