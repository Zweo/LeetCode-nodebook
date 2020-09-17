原题：[Leetcode冗余连接II](https://leetcode-cn.com/problems/redundant-connection-ii/)

一份很烂的代码，留给之后的自己看看曾经自己多么菜（泪目……）好歹是手写出来的困难题。

```python
class Solution:
    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        edge = [[] for _ in range(N + 1)]
        inv_edge = [[] for _ in range(N + 1)]

        cir = []

        def get_circle(edge, cur_edge):
            if cur_edge[1] == cir[0][0]:
                return True
            if len(cir) > N:
                return False
            for v in edge[cur_edge[1]]:
                item = [cur_edge[1], v]
                cir.append(item)
                if get_circle(edge, item):
                    return True
                cir.pop()
            return False

        uv = []
        uv2 = []
        for item in edges:
            u, v = item
            edge[u].append(v)
            inv_edge[v].append(u)
            if edge[v]:
                uv.append(item)
            if len(inv_edge[v]) == 2:  # 有两个父节点，必定去掉其中一个（在环中的）
                uv2 = [[x, v] for x in inv_edge[v]]

        if uv:
            for i in range(len(uv) - 1, -1, -1):
                cir.append(uv[i])  # 找到环,记录环
                if get_circle(edge, uv[i]):
                    break
                cir = []
            if uv2:  # 有两个父节点的，去掉在环中的
                if cir:
                    for t in uv2:
                        if t in cir:
                            return t
                else:
                    return uv2[1]
            else:  # 无两个父节点的，去掉环最后出现的边
                return cir[0]
        elif uv2:  # 有两父节点，无环（有向环）,去掉第二次出现的
            return uv2[1]

        return []
  ```
