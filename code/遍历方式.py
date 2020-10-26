def traverse(root: TreeNode):
    if not root:
        return
    # 前序遍历
    traverse(root.left)
    # 中序遍历
    traverse(root.right)
    # 后序遍历


def path(root: TreeNode):
    '''层次遍历'''
    queue = [root]
    while queue:
        cur = queue.pop()
        queue.append(root.left) if root.left else None
        queue.append(root.right) if root.right else None
        print(cur.val)


def inorderTraversal(self, root: TreeNode):
    '''迭代形式中序遍历'''
    res = []
    track = [root]
    while track:
        cur = track.pop()
        if isinstance(cur, TreeNode):
            track.extend([cur.right, cur.val, cur.left])
        elif isinstance(cur, int):
            res.append(cur)
    return res


def postorderTraversal(self, root: TreeNode):
    '''迭代形式后序遍历'''
    res = []
    track = [root]
    while track:
        cur = track.pop()
        if isinstance(cur, TreeNode):
            track.extend(cur.val, [cur.right, cur.left])
        elif isinstance(cur, int):
            res.append(cur)
    return res
