# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        k = 0

        while q:
            lvl_list = []
            len_q = len(q)
            for i in range(len_q):
                node = q.popleft()
                if node:
                    lvl_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if lvl_list:
                if k %2 == 0:
                    res.append(lvl_list)
                else:
                    res.append(lvl_list[::-1])

            k += 1

        return res
        
