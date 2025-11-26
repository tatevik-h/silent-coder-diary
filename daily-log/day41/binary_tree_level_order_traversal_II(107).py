# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

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
                res.append(lvl_list)
        
        return res[::-1]
      
