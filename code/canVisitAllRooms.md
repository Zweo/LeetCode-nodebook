# 1. 问题

[Leetcode原题地址](https://leetcode-cn.com/problems/keys-and-rooms/)

有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

如果能进入每个房间返回 true，否则返回 false。

示例：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200831132342208.png#pic_center)




# 2.思路
用一个数组存储某个房间是否已经访问过。
返回：所有房间是否均已访问

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        isvisited = [False for _ in range(len(rooms))]

        def dfs(cur):
            if isvisited[cur]:
                return
            isvisited[cur] = True
            for item in rooms[cur]: 
                dfs(item)

        dfs(0)

        return all(isvisited)
```
用all判断时间耗费较长，如果使用字典，可以稍微缩短时间：
```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        isvisited = {}

        def dfs(cur):
            if cur in isvisited:
                return
            isvisited[cur] = True
            for item in rooms[cur]: 
                dfs(item)

        dfs(0)

        return len(isvisited) == len(rooms)
```




# 3.优化

把递归改成循环，可以再提升一点速度。
