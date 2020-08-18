
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        res = TreeNode(head.val)
        head = head.next
        cur = res
        queue = []
        i = 1
        while head:
            if i % 2:
                cur.left = TreeNode(head.val)
                queue.append(cur.left)
            else:
                cur.right = TreeNode(head.val)
                queue.append(cur.left)
                cur = queue.pop(0)
            i += 1
            head = head.next
        return res
