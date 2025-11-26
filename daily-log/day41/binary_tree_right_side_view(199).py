## option 1
# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)
        rnode = None

        while q:
            lvl_list = []
            len_q = len(q)

            for i in range(len_q):
                node = q.popleft()
                rnode = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(rnode)
        
        return res


## option 2
# Definition for a binary tree node.
# class TreeNode(object):
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        res = []

        def dfs(node,lvl):
            if not node:
                return []
            if lvl == len(res):
                res.append(node.val)
            
            dfs(node.right,lvl +1)
            dfs(node.left, lvl +1)

        dfs(root,0)
        
        return res
      
