class Solution:
    def countSubstrings(self, s: str) -> int:
        str_len = len(s)
        res = str_len

        def fuc(left, right):
            if left < 0 or right >= str_len:
                return 0
            if s[left] == s[right]:
                return fuc(left - 1, right + 1) + 1
            return 0

        for i in range(str_len - 1):
            for j in [i + 1, i + 2]:
                # j = i + 1 判断偶数回文,i+2判断奇数
                if j < str_len and s[i] == s[j]:
                    res += 1
                    res += fuc(i - 1, j + 1)

        return res
