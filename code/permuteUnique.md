
### 解题思路
[原题地址](https://leetcode-cn.com/problems/permutations-ii/)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020091821273956.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjE2NTU4NQ==,size_16,color_FFFFFF,t_70#pic_center)


回溯问题已经熟练起来了，掌握了套路，我这个菜鸡也能写出好算法。
首先搬出回溯问题**框架**：
```python
    def dfs():
        res = []
        def backtrack(track):
            if 结束条件：
                res.append()
                return
            for num in 可选项:
                做选择
                backtrack(track) 进入下一层
                撤销选择
        backtrack(track)
        return res
```

那么写出第一版就很简单了。

**结束条件：** 当路径达到nums的长度N
**可选项：** 去除已经选择的数字，nums中剩余的数字
        
- 这里用pop读取第一个数字，之后当前读取的数字就不会在可选的范围内
- 每次返回上一层时候，将这个数字添加到末尾，保持nums的长度不会改变，然后pop会读取下一个数字。

 
res : 保存最终结果
track : 记录遍历路径（这里使用track + [] 传参的方法，相当于append和pop）

```python3
class Solution:
    def permuteUnique(self, nums):
        res = []
        N = len(nums)
        def backtrack(track):
            if len(track) == N:
                res.append(track)
                return
            for _ in nums:
                item = nums.pop(0)
                backtrack(track + [item])
                nums.append(item)
        backtrack([])
        return res
```

然后这样会出现重复的排列，怎样通过简单的方式去重呢？不必走到最后再去排队res中是否存在已有排列。
画一个决策树：

![image.png](https://img-blog.csdnimg.cn/img_convert/65edb35f3e9830334faebeab2b59b43a.png)

可以通过观察发现一个规律：**只要在当前层（递归层数）出现过这个数字**，后面的就不用看了。
所以可以通过一个列表记录一下，如下方的shown数组。


### 代码

```python3
class Solution:
    def permuteUnique(self, nums):
        res = []
        N = len(nums)

        def backtrack(track):
            if len(track) == N:
                res.append(track)
                return
            shown = []
            for _ in nums:
                item = nums.pop(0)
                if item in shown:
                    nums.append(item)
                    continue
                backtrack(track + [item])
                shown.append(item)
                nums.append(item)

        backtrack([])

        return res
```

欢迎star
