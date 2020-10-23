### 解题思路

https://leetcode-cn.com/problems/palindrome-linked-list/

存进数组，判断是否回文

### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]
```
