class Solution:
    def sortByBits(self, arr):
        def countOne(num):
            cnt = 0
            r_num = num
            while r_num:
                cnt += r_num & 1
                r_num >>= 1
            return cnt, num

        return sorted(arr, key=countOne)
